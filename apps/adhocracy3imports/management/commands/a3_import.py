from functools import lru_cache

import requests
import requests.adapters
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import CommandError
from django.utils import timezone

from adhocracy4.comments.models import Comment
from adhocracy4.modules.models import Module
from adhocracy4.phases.models import Phase
from adhocracy4.projects.models import Project
from adhocracy4.ratings.models import Rating
from apps.users.models import User

from .a3_import_users import fixup_username


def get_organisation_model():
    """
    Return the Organisation model that is active in this project.
    """
    try:
        return django_apps.get_model(
            settings.A4_ORGANISATIONS_MODEL,
        )
    except ValueError:
        raise ImproperlyConfigured(
            "A4_ORGANISATIONS_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            (
                "A4_ORGANISATIONS_MODEL refers to model '%s'"
                " that has not been installed"
            ).format(settings.A4_ORGANISATIONS_MODEL)
        )

Organisation = get_organisation_model()


def parse_dt(date_str):
    # remove colon in timezone offset
    parts = date_str.split(':')
    minutes_offset = parts.pop()
    date_str = ':'.join(parts) + minutes_offset

    date = timezone.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
    return date


class A3ImportCommandMixin():

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='a3 API url')
        parser.add_argument('api_user', type=str, help='a3 API admin user')
        parser.add_argument('api_password', type=str,
                            help='a3 API admin user password')
        parser.add_argument('creator', type=str, help='a4 creator username')

    def handle(self, *args, **options):
        if settings.EMAIL_BACKEND != \
                'django.core.mail.backends.dummy.EmailBackend':
            raise CommandError('Set EMAIL_BACKEND to '
                               'django.core.mail.backends.dummy.EmailBackend.')

        url = options.get('url')
        username = options.get('api_user')
        password = options.get('api_password')
        creator = options.get('creator')
        default_creator = User.objects.get(username=creator)

        self.session = requests.Session()
        self.session.mount(
            url,
            requests.adapters.HTTPAdapter(max_retries=5)

        )

        self.a3_login(url, username, password)
        self.default_creator = default_creator
        fallback_creator, _created = User.objects.get_or_create(
            username='unkown',
            email='do-not-reply@liqd.net',
            password='invalid',
        )
        self.fallback_creator = fallback_creator

    def a3_login(self, url, username, password):
        login_url = url + 'login_username'
        res = self.session.post(
            login_url,
            json={'name': username, 'password': password}
        )
        if res.status_code != requests.codes.ok:
            raise CommandError('API user authentication failed.')
        self.token = res.json()['user_token']
        return self.token

    def a3_get_elements(self, url, resource_type, elements,
                        depth='all', additional_filter=None):
        query_url = '{}?content_type={}&depth={}&elements={}'.format(
            url, resource_type, depth, elements
        )
        if additional_filter:
            query_url = (
                query_url + '&' + additional_filter[0] +
                '=' + additional_filter[1]
            )
        if 'Version' in resource_type:
            query_url = query_url + '&tag=LAST'
        res = self.session.get(query_url, headers={'X-User-Token': self.token})
        if res.status_code != requests.codes.ok:
            raise CommandError('Request failed for URL: {}'.format(query_url))
        data = res.json()
        paths = data['data']['adhocracy_core.sheets.pool.IPool']['elements']
        return paths

    @lru_cache(maxsize=None)
    def a3_get_resource(self, resource_url):
        res = self.session.get(
            resource_url,
            headers={'X-User-Token': self.token}
        )
        if res.status_code != requests.codes.ok:
            raise CommandError('Request failed for URL: {}'.format(
                resource_url)
            )
        data = res.json()
        return data

    def a3_get_sheet_field(self, resource_url, sheet, field):
        data = self.a3_get_resource(resource_url)
        sheet_field_value = data['data'][sheet][field]
        return sheet_field_value

    def a3_get_last_version(self, resorce_path):
        return self.a3_get_sheet_field(
            resorce_path,
            'adhocracy_core.sheets.tags.ITags',
            'LAST'
        )

    def a3_get_creation_date(self, path):
        date_str = self.a3_get_sheet_field(
            path, self.token,
            'adhocracy_core.sheets.metadata.IMetadata', 'creation_date')
        date = parse_dt(date_str)
        return date

    def a3_get_modification_date(self, path):
        date_str = self.a3_get_sheet_field(
            path, self.token,
            'adhocracy_core.sheets.metadata.IMetadata', 'modification_date')
        date = parse_dt(date_str)
        return date

    def a3_get_user_by_path(self, path):
        username = self.a3_get_sheet_field(
            path,
            'adhocracy_core.sheets.principal.IUserBasic',
            'name'
        )
        user = User.objects.get(username=fixup_username(username))
        return user

    def a3_import_comment(self, comment_path, object_path,
                          content_object):
        comment = None
        comment_resource = self.a3_get_resource(comment_path)
        data = comment_resource['data']
        metadata_sheet = data['adhocracy_core.sheets.metadata.IMetadata']
        is_hidden = metadata_sheet['hidden']
        user_path = metadata_sheet['creator']
        creation_date = parse_dt(metadata_sheet['creation_date'])
        last_version_path = self.a3_get_last_version(comment_path)
        last_version = self.a3_get_resource(last_version_path)
        data = last_version['data']
        if is_hidden == 'false' and user_path:
            comment_sheet = data['adhocracy_core.sheets.comment.IComment']
            object = comment_sheet['refers_to']
            if object_path == object:
                user = self.a3_get_user_by_path(user_path)
                content = comment_sheet['content']
                (comment, _created) = Comment.objects.update_or_create(
                    creator=user,
                    created=creation_date,
                    defaults={
                        'content_object': content_object,
                        'comment': content,
                    },
                )
        return comment

    def a3_import_comments(self, object_path, content_object):
        comments_path = self.a3_get_sheet_field(
            object_path,
            'adhocracy_core.sheets.comment.ICommentable', 'post_pool')
        comment_paths = self.a3_get_elements(
            comments_path,
            'adhocracy_core.resources.comment.IComment', 'paths')
        for comment_path in comment_paths:
            comment = self.a3_import_comment(
                comment_path, object_path, content_object)

            if comment:
                comment_version_path = \
                    self.a3_get_last_version(comment_path)
                self.a3_import_ratings(
                    comment_version_path, comment)
                self.a3_import_comment_replies(
                    comment_paths, comment_version_path, comment)

    def a3_import_comment_replies(self, comment_paths,
                                  comment_version_path, content_object):
        for comment_path in comment_paths:
            reply = self.a3_import_comment(
                comment_path, comment_version_path, content_object)
            if reply:
                reply_version_path = \
                    self.a3_get_last_version(comment_path)
                self.a3_import_ratings(comment_version_path, reply)
                self.a3_import_comment_replies(
                    comment_paths, reply_version_path,
                    content_object)

    def a3_import_ratings(self, object_path, content_object):
        rates_path = self.a3_get_sheet_field(
            object_path,
            'adhocracy_core.sheets.rate.IRateable',
            'post_pool'
        )
        rates_content = self.a3_get_elements(
            rates_path,
            'adhocracy_core.resources.rate.IRateVersion',
            'content',
            additional_filter=(
                'adhocracy_core.sheets.rate.IRate:object',
                object_path
            )
        )
        for rate_resource in rates_content:
            data = rate_resource['data']
            metadata_sheet = data['adhocracy_core.sheets.metadata.IMetadata']
            is_hidden = metadata_sheet['hidden']
            rate_sheet = data['adhocracy_core.sheets.rate.IRate']
            user_path = rate_sheet['subject']
            is_object = rate_sheet['object'] == object_path
            if is_hidden == 'false' and user_path and is_object:
                creation_date = parse_dt(metadata_sheet['creation_date'])
                user = self.a3_get_user_by_path(user_path)
                rate_value = int(rate_sheet['rate'])
                if rate_value != 0:
                    Rating.objects.update_or_create(
                        creator=user,
                        created=creation_date,
                        defaults={
                            'value': rate_value,
                            'content_object': content_object,
                        },
                    )

    def a3_get_rates(self, resource_path, object_path):
        rates_path = resource_path + 'rates/'
        rates = []
        rates_content = self.a3_get_elements(
            rates_path, self.token,
            'adhocracy_core.resources.rate.IRateVersion', 'content')
        for rate in rates_content:
            data = rate['data']
            is_hidden = \
                data['adhocracy_core.sheets.metadata.IMetadata']['hidden']
            rate_sheet = data['adhocracy_core.sheets.rate.IRate']
            user_path = rate_sheet['subject']
            is_object = rate_sheet['object'] == object_path
            if is_hidden == 'false' and user_path and is_object:
                user = self.a3_get_user_by_path(user_path)
                rate_value = int(rate_sheet['rate'])
                if rate_value != 0:
                    rates.append((user, rate_value))
        return rates

    def a3_get_dates(self, path, wt):
        creation_date = wt.get('created')
        if not creation_date:
            creation_date = self.a3_get_creation_date(path, self.token)
        modification_date = wt.get('modified')
        if not modification_date:
            modification_date = self.a3_get_modification_date(path, self.token)
        return (creation_date, modification_date)

    def create_project(self, organisation, name, description, info, start_date,
                       end_date, is_draft, is_archived, phase_contents, typ='',
                       slug=None):

        if slug:
            project, created = Project.objects.update_or_create(
                slug=slug,
                defaults={
                    "name": name,
                    "description": description,
                    "information": info,
                    "is_draft": is_draft,
                    "is_archived": is_archived,
                    "typ": typ,
                    "organisation": organisation,
                    "created": start_date,
                }
            )

            project.phases.delete()
            module, _created = project.module_set.update_or_create(
                weight=1,
                defaults={
                    "name": project.slug + '_module',
                }
            )
        else:
            project = Project.objects.create(
                name=name,
                description=description,
                information=info,
                is_draft=is_draft,
                is_archived=is_archived,
                typ=typ,
                organisation=organisation,
                created=start_date,
                slug=slug,
            )

            module = Module.objects.create(
                name=project.slug + '_module',
                weight=1,
                project=project,
            )

        phase_start = start_date
        phase_duration = (end_date - start_date) / len(phase_contents)
        for phase_content in phase_contents:
            phase_end = phase_start + phase_duration
            Phase.objects.create(
                name=phase_content.name,
                description=phase_content.description,
                type=phase_content.identifier,
                module=module,
                start_date=phase_start,
                end_date=phase_end
            )
            phase_start = phase_end

        return (project, module)
