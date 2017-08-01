import datetime
from os import path
from urllib.parse import urlparse

import requests
from django.core.exceptions import ValidationError
from django.core.files import base, images
from django.core.management.base import BaseCommand
from django.db.models import CharField
from django.utils import timezone

from apps.ideas import models, phases

from .a3_import import A3ImportCommandMixin, get_organisation_model, parse_dt

Organisation = get_organisation_model()


organisation_status_map = {
    'registered_nonprofit': 'non_profit',
    'planned_nonprofit': 'non_profit_planned',
    'support_needed': 'no_non_profit',
}


heard_froms_map = {
    'website': 'websites',
}


country_map = {
    'XK': ''  # Kosovo doesn't have an offical ISO-3166 code yet
}


def translate_idea_topic(topics):
    return [t.replace('_and_', '_') for t in topics if t != 'other']


def download_file(asset_url):
    response = requests.get(asset_url)
    data = response.json()['data']
    img_url = data[
        'adhocracy_mercator.sheets.mercator.IIntroImageMetadata']['detail']
    response = requests.get(img_url)
    filename = path.split(path.split(asset_url)[0])[1]
    return images.ImageFile(base.ContentFile(response.content), filename)


def parse_year(date_str):
    # remove colon in timezone offset
    parts = date_str.split(':')
    minutes_offset = parts.pop()
    date_str = ':'.join(parts) + minutes_offset

    date = timezone.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
    return date.year


def parse_heard_froms(heard_froms):
    value = heard_froms[0]
    return heard_froms_map.get(value, value)


def floatstr_to_int(float_str):
    return int(float(float_str))


class Command(A3ImportCommandMixin, BaseCommand):

    sheet_map = {
        "adhocracy_mercator.sheets.mercator2.IOrganizationInfo": [
            ("status", "organisation_status", organisation_status_map),
            ("country", "organisation_country"),
            ("name", "organisation_name"),
            ("city", "organisation_city"),
            # ("help_request", "???"),
            ("status_other", "organisation_status_extra"),
            ("registration_date", "year_of_registration", parse_year),
            ("website", "organisation_website"),
        ],
        # "adhocracy_mercator.sheets.mercator2.IStatus": [
        # ("status", "???"), # eg developing starting
        # ],
        "adhocracy_mercator.sheets.mercator2.ILocation": [
            # ("has_link_to_ruhr", "false"),
            ("link_to_ruhr", "idea_location_ruhr"),
            ("location", "idea_location_specify"),
            # ("is_online", "false"),
        ],
        "adhocracy_mercator.sheets.mercator2.IFinancialPlanning": [
            ("budget", "total_budget", floatstr_to_int),
            ("requested_funding", "budget_requested", floatstr_to_int),
            ("major_expenses", "major_expenses"),
        ],
        "adhocracy_mercator.sheets.mercator2.IUserInfo": [
            ("first_name", "first_name"),
            ("last_name", "last_name"),
        ],
        "adhocracy_mercator.sheets.mercator2.ICommunity": [
            ("heard_froms", "how_did_you_hear", parse_heard_froms),
            ("expected_feedback", "reach_out"),
            # ("heard_from_other", "")
        ],
        "adhocracy_core.sheets.title.ITitle": [
            ("title", "idea_title")
        ],
        "adhocracy_mercator.sheets.mercator2.ITopic": [
            ("topic", "idea_topics", translate_idea_topic),
            ("topic_other", "idea_topics_other"),
        ],
        "adhocracy_core.sheets.image.IImageReference": [
            ("picture", "idea_image", download_file)
        ],
    }

    subresource_map = {
        'adhocracy_mercator.resources.mercator2.IPartners': {
            'adhocracy_mercator.sheets.mercator2.IPartners': [
                ('partner1_name', 'partner_organisation_1_name'),
                ('partner1_website', 'partner_organisation_1_website'),
                ('partner1_country',
                 'partner_organisation_1_country', country_map),
                ('partner2_name', 'partner_organisation_2_name'),
                ('partner2_website', 'partner_organisation_2_website'),
                ('partner2_country',
                 'partner_organisation_2_country', country_map),
                ('partner3_name', 'partner_organisation_3_name'),
                ('partner3_website', 'partner_organisation_3_website'),
                ('partner3_country',
                 'partner_organisation_3_country', country_map),
                ('other_partners', 'partners_more_info'),
            ]
        },
        'adhocracy_mercator.resources.mercator2.IChallenge': {
            # WHAT IS THE CHALLENGE YOU ARE ADDRESSING?
            'adhocracy_mercator.sheets.mercator2.IChallenge': [
                ('challenge', 'challenge')
            ]
        },
        'adhocracy_mercator.sheets.mercator2.IPracticalRelevance': {
            # WHAT IS THE PRACTICAL RELEVANCE OF YOUR IDEA TO THE
            # EVERYDAY LIVES OF PEOPLE IN EUROPE?
            'adhocracy_mercator.sheets.mercator2.IPracticalRelevance': [
                ('practicalrelevance', 'selection_relevance')
            ]
        },
        'adhocracy_mercator.resources.mercator2.ITeam': {
            # WHO IS PART OF YOUR PROJECT TEAM?
            'adhocracy_mercator.sheets.mercator2.ITeam': [
                ('team', 'members')
            ]
        },
        # 'adhocracy_mercator.resources.mercator2.IExtraInfo': {
        # WHAT ELSE SHOULD WE KNOW ABOUT YOU OR YOUR PROJECT IDEA?
        #     'adhocracy_mercator.sheets.mercator2.IExtraInfo': [
        #         ('extrainfo', '???')
        #     ]
        # },
        'adhocracy_mercator.resources.mercator2.ITarget': {
            # WHO ARE YOU DOING IT FOR?
            'adhocracy_mercator.sheets.mercator2.ITarget': [
                ('target', 'target_group')
            ]
        },
        'adhocracy_mercator.resources.mercator2.IDuration': {
            # DURATION OF PROJECT (MONTHS)
            'adhocracy_mercator.sheets.mercator2.IDuration': [
                ('duration', 'duration')
            ]
        },
        'adhocracy_mercator.resources.mercator2.IConnectionCohesion': {
            # HOW WILL YOUR PROJECT IDEA STRENGTHEN CONNECTION AND COHESION
            # IN EUROPE?
            'adhocracy_mercator.sheets.mercator2.IConnectionCohesion': [
                ('connection_cohesion', 'selection_cohesion')
            ]
        },
        'adhocracy_mercator.resources.mercator2.IGoal': {
            # WHAT ARE YOU AIMING FOR?
            'adhocracy_mercator.sheets.mercator2.IGoal': [
                ('goal', 'outcome')
            ]
        },
        'adhocracy_mercator.resources.mercator2.IPitch': {
            # Your idea in brief
            'adhocracy_mercator.sheets.mercator2.IPitch': [
                ('pitch', 'idea_pitch')
            ]
        },
        'adhocracy_mercator.resources.mercator2.IDifference': {
            # WHAT MAKES YOUR IDEA DIFFERENT FROM OTHERS?
            'adhocracy_mercator.sheets.mercator2.IDifference': [
                ('difference', 'selection_apart')
            ]
        },
        'adhocracy_mercator.resources.mercator2.IPlan': {
            # HOW DO YOU PLAN TO GET THERE?
            'adhocracy_mercator.sheets.mercator2.IPlan': [
                ('plan', 'plan')
            ]
        }
    }

    def handle(self, *args, **options):
        """
        URL maps required

        /en/winners$ => Projects.objects.get(slug='ae2015').get_absolute_url()
        /en/idea-space$ =>
            Projects.objects.get(slug='ae2016').get_absolute_url()
        /en/idea-space#!/r/advocate-europe/2016/(?P<slug>[^/])/(.*)$ =>
            Ideas.object.get(slug=slug).get_absolute_url()
        """
        super().handle(*args, **options)

        project_urls = {
            2016: (
                'https://frontend.advocate-europe.eu/api/advocate-europe/2016/'
            ),
            2015: 'https://frontend.advocate-europe.eu/api/mercator/',
        }

        project, module = self.create_ae_project(2016)
        self.import_all_proposals(project, module, project_urls[2016])

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

        new = item_cls(
            creator=self.a3_get_user_by_path(metadata['creator']),
            created=parse_dt(metadata['creation_date']),
            modified=parse_dt(metadata['modification_date'])
        )

        return new, True

    def a3_copy_subresource_data(self, item, a3_resource, mapping):
        """
        Assumes that the resource has be requested with elements=content.
        """

        pool_sheet = a3_resource['data']['adhocracy_core.sheets.pool.IPool']
        elements = pool_sheet['elements']
        for element in elements:
            assert type(element) is dict

            if element['content_type'] in mapping:
                sheet_mapping = mapping[element['content_type']]
                self.a3_copy_sheet_data(item, element, sheet_mapping)

    def a3_copy_sheet_data(self, item, a3_resource, mapping):
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

    def import_all_proposals(self, project, module, project_url):
        proposal_ct = (
            'adhocracy_mercator.resources.mercator2.IMercatorProposal'
        )
        urls = self.a3_get_elements(project_url, proposal_ct, 'paths')

        for url in urls:
            a3proposal = self.a3_get_resource(url + '?elements=content')

            (_rest, slug) = path.split(path.split(urlparse(url).path)[0])
            a4proposal, created = self.a3_item_get_or_create(
                models.Proposal, a3proposal, slug=slug
            )

            if not a4proposal:
                print("SKIP: {}".format(url))
                continue
            else:
                print("STRT: {}".format(url))

            if created:
                a4proposal.slug = slug

            a4proposal.module = module

            # copy data from sheets
            self.a3_copy_sheet_data(a4proposal, a3proposal, self.sheet_map)

            # copy data from subressource
            self.a3_copy_subresource_data(
                a4proposal, a3proposal, self.subresource_map
            )

            # create archived idea sketch
            archive = models.IdeaSketchArchived.objects.filter(
                slug=slug).first()
            if not archive:
                archive = models.IdeaSketchArchived(
                    creator=a4proposal.creator,
                    module=a4proposal.module,
                )

            # a lot of fields have bigger lengths in A3, so the need to be
            # trimmed
            for field in a4proposal._meta.get_fields():
                if isinstance(field, CharField):
                    value = getattr(a4proposal, field.name, '')
                    if field.max_length < len(value):
                        print(
                            "Cutting {} with value {}".format(
                                field.name, value
                            )
                        )
                        setattr(
                            a4proposal, field.name, value[:field.max_length]
                        )

            proposal_fields = [
                f.name for f in a4proposal._meta.get_fields()
                if not f.is_relation
            ]
            archive_fields = [
                f.name for f in archive._meta.get_fields()
            ]
            for field_name in proposal_fields:
                if field_name in archive_fields:
                    setattr(
                        archive, field_name, getattr(a4proposal, field_name)
                    )

            # fill previously non-existing fields
            archive.collaboration_camp_option = 'not_sure'
            archive.collaboration_camp_represent = (
                'When this idea was created, '
                'the collaboration camp did not exist.'
            )
            archive.collaboration_camp_email = 'noreply@advocate-europe.eu'
            archive.collaboration_camp_benefit = 'No expections.'
            archive.importance = (
                'When this idea was created, this field did not exist.'
            )
            a4proposal.importance = (
                'When this idea was created, this field did not exist.'
            )
            a4proposal.selection_relevance = (
                'When this idea was created, this field did not exist.'
            )

            # TODO: image is not set

            try:
                archive.full_clean(exclude=['idea_title'])
                a4proposal.full_clean(
                    exclude=['idea_title', 'idea_sketch_archived'])
            except ValidationError as e:
                print("ABRT: {}".format(url))
                from pprint import pprint
                pprint(e.error_dict)
                import pdb
                pdb.set_trace()
                raise
            except:
                print("ABRT: {}".format(url))
                raise

            archive.save()
            a4proposal.idea_sketch_archived = archive
            a4proposal.save()

            # TODO: copy comments
            # TODO: copy rates
            # TODO: copy logbook
            # TODO: transform badge into state (what about jury verdict?)

            if created:
                print("INIT: {}".format(url))
            else:
                print("UPDT: {}".format(url))
