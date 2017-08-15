import datetime
import sys
import traceback
from os import path
from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

from apps.ideas import models, phases

from .a3_import import A3ImportCommandMixin, get_organisation_model, parse_dt

Organisation = get_organisation_model()

DEFAULT_VALUE = '-'


class Sheets:
    DESCRIPTION = 'adhocracy_core.sheets.description.IDescription'
    BADGEBALE = 'adhocracy_core.sheets.badge.IBadgeable'
    BADGE_ASSIGNMENT = 'adhocracy_core.sheets.badge.IBadgeAssignment'
    NAME = 'adhocracy_core.sheets.name.IName'


class Command(A3ImportCommandMixin, BaseCommand):

    def handle(self, *args, **options):
        """
        Import adhocracy3 advocate europe projects from 2015 and 2016.a

        Following URL maps could be applied in deployment to keep the urls
        working. Beware that a few slug modifications have been applied.

        /en/winners$ => Projects.objects.get(slug='ae2015').get_absolute_url()
        /en/idea-space$ =>
            Projects.objects.get(slug='ae2016').get_absolute_url()
        /en/idea-space#!/r/advocate-europe/2016/(?P<slug>[^/])/(.*)$ =>
            Ideas.object.get(slug=slug).get_absolute_url()
        """
        super().handle(*args, **options)

        project, module = self.create_ae_project(2015)
        self.import_all_proposals(project, module, 2015)

        project, module = self.create_ae_project(2016)
        self.import_all_proposals(project, module, 2016)

    def create_ae_project(self, year):
        organisation, _created = Organisation.objects.update_or_create(
            pk=1,
            defaults={
                'name': 'Stiftung Mercator'
            }
        )

        phase_contents = [
            phases.IdeaSketchPhase(),
            phases.FullProposalPhase(),
        ]

        return self.create_project(
            organisation,
            'Idea challenge {}'.format(year),
            description='lorem ipsum',
            info='lorem impsum',
            start_date=datetime.datetime(
                year, 1, 1,
                tzinfo=datetime.timezone.utc
            ),
            end_date=datetime.datetime(
                year, 12, 31,
                tzinfo=datetime.timezone.utc
            ),
            is_draft=False,
            is_archived=False,
            phase_contents=phase_contents,
            slug='ae{}'.format(year),
        )

    def a3_item_get_or_create(self, item_cls, a3_resource, **kwargs):

        if kwargs:
            exisiting = item_cls.objects.filter(**kwargs).first()

            if exisiting:
                return exisiting, False

        metadata = a3_resource['data'][
            'adhocracy_core.sheets.metadata.IMetadata']

        if metadata['deleted'] == 'true' or metadata['hidden'] == 'true':
            return None, None

        if metadata['creator']:
            creator = self.a3_get_user_by_path(metadata['creator'])
        else:
            creator = self.fallback_creator

        new = item_cls(
            creator=creator,
            created=parse_dt(metadata['creation_date']),
            modified=parse_dt(metadata['modification_date']),
            **kwargs
        )

        return new, True

    def a3_copy_subresource_data(
            self, item, a3_resource, mapping, resources_are_versionable=False
    ):
        """
        Assumes that the resource has be requested with elements=content.
        """
        pool_sheet = a3_resource['data']['adhocracy_core.sheets.pool.IPool']
        elements = pool_sheet['elements']
        for element in elements:
            assert type(element) is dict

            if element['content_type'] in mapping:
                sheet_mapping = mapping[element['content_type']]
                self.a3_copy_sheet_data(
                    item,
                    element,
                    sheet_mapping,
                    resources_are_versionable
                )

    def a3_get_batches(self, a3resource):
        """
        Extract badge name and description of the assignment if it exists.
        """
        result = {}
        a_urls = a3resource['data'][Sheets.BADGEBALE]['assignments']

        for assignment_url in a_urls:
            assign = self.a3_get_resource(assignment_url)
            description = assign['data'][Sheets.DESCRIPTION]['description']
            badge_url = assign['data'][Sheets.BADGE_ASSIGNMENT]['badge']
            badge = self.a3_get_resource(badge_url)
            name = badge['data'][Sheets.NAME]['name']
            result[name] = description
        return result

    def a3_copy_sheet_data(
            self, item, a3_resource, mapping, resource_is_versionable
    ):
        if resource_is_versionable:
            data = a3_resource['data']
            tags = data['adhocracy_core.sheets.tags.ITags']
            last_version = tags['LAST']
            a3_resource = self.a3_get_resource(last_version)

        data = a3_resource['data']
        for sheet, fieldspec in mapping.items():
            for src_field, *actions in fieldspec:
                dst_field = actions[0]
                src_value = data[sheet][src_field]

                if len(actions) == 1:
                    value = src_value
                elif callable(actions[1]):
                    transform = actions[1]
                    if src_value is None:
                        value = None
                    else:
                        value = transform(src_value)
                else:
                    map = actions[1]
                    value = map.get(src_value, src_value)

                setattr(item, dst_field, value)

    def import_all_proposals(self, project, module, year):
        if year == 2015:
            from .variants import ae2015 as v
        else:
            from .variants import ae2016 as v

        urls = self.a3_get_elements(v.project_url, v.proposal_ct, 'paths')

        for url in urls:
            a3proposal = self.a3_get_resource(url + '?elements=content')

            if v.resources_are_versionable:
                last_version_url = self.a3_get_last_version(url)
            else:
                last_version_url = url

            # parse slug and fix up differences between slugify implementations
            (_rest, slug) = path.split(path.split(urlparse(url).path)[0])
            slug = slugify(slug)[0:50]

            a4proposal, created = self.a3_item_get_or_create(
                models.Proposal, a3proposal, slug=slug
            )

            if not a4proposal:
                print("SKIP: {}".format(url))
                continue
            else:
                print("STRT: {}".format(url))

            a4proposal.module = module

            # copy data from sheets
            self.a3_copy_sheet_data(
                a4proposal,
                a3proposal,
                v.sheet_map,
                v.resources_are_versionable
            )

            # copy data from subressource
            self.a3_copy_subresource_data(
                a4proposal,
                a3proposal,
                v.subresource_map,
                v.resources_are_versionable
            )

            # set title from subtitle
            subtitle = a4proposal.idea_subtitle
            if len(subtitle) < 50:
                title = subtitle
                subtitle = ''
            else:
                pos = -1
                for mark in ':–-':
                    pos = subtitle[:50].rfind(mark)

                    if pos > 0:
                        break

                if pos > 0:
                    title = subtitle[:pos].strip()
                    subtitle = subtitle[pos+1:].strip()
                else:
                    pos = subtitle[:49].rfind(' ')

                    if pos == -1:
                        pos = 49

                    title = subtitle[:pos] + ' …'
                    subtitle = '… ' + subtitle[pos+1:].strip()
            a4proposal.idea_subtitle = subtitle
            a4proposal.idea_title = title

            # set default values for newly introduced fields
            for name in v.default_fields:
                value = None
                if not isinstance(name, str):
                    value = name[1]
                    name = name[0]
                setattr(a4proposal, name, value or DEFAULT_VALUE)

            # create archived idea sketch and copy data
            archive = models.IdeaSketchArchived.objects.filter(
                idea__slug=slug).first()
            if not archive:
                archive = models.IdeaSketchArchived(
                    creator=a4proposal.creator,
                )

            proposal_fields = [
                f.name for f in a4proposal._meta.get_fields()
                if not f.is_relation
            ]
            archive_fields = [
                f.name for f in archive._meta.get_fields()
                if not f.primary_key
                and not f.is_relation
            ]
            for field_name in proposal_fields:
                if field_name in archive_fields:
                    setattr(
                        archive, field_name, getattr(a4proposal, field_name)
                    )

            # gather information from badges
            badges = self.a3_get_batches(
                self.a3_get_resource(last_version_url)
            )

            a4proposal.is_winner = 'winning' in badges
            a4proposal.jury_statement = badges.get('winning', '')
            a4proposal.is_on_shortlist = 'shortlist' in badges
            a4proposal.community_award_winner = 'community' in badges

            # fill collaboration camp fields
            archive.collaboration_camp_option = 'not_sure'
            archive.collaboration_camp_represent = DEFAULT_VALUE
            archive.collaboration_camp_email = 'noreply@advocate-europe.eu'
            archive.collaboration_camp_benefit = DEFAULT_VALUE

            try:
                archive.full_clean(exclude=['idea'])
                a4proposal.full_clean()
            except ValidationError as e:
                print("SKIP: {}".format(url))
                from pprint import pprint
                pprint(e.error_dict)
                continue
            except:
                print("ABRT: {}".format(url))
                raise

            try:
                with transaction.atomic():
                    a4proposal.save()

                    archive.idea = a4proposal.idea
                    archive.save()
            except:
                print("SKIP: {}".format(url))
                exc_type, exc_value, exc_traceback = sys.exc_info()
                lines = traceback.format_exception(
                    exc_type,
                    exc_value,
                    exc_traceback
                )
                print('\n'.join(lines))
                continue

            self.a3_import_comments(last_version_url, a4proposal.idea)

            if created:
                print("INIT: {}".format(url))
            else:
                print("UPDT: {}".format(url))
