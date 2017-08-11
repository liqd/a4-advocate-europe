from .helpers import download_file, floatstr_to_int, parse_year

# Sheets and subresources that still require mapping:
#
# status sheet: ???
# extra info subresource: WHAT ELSE SHOULD WE KNOW ABOUT YOU OR YOUR PROJECT
#                         IDEA?

project_url = (
    'https://frontend.advocate-europe.eu/api/advocate-europe/2016/'
)


proposal_ct = (
    'adhocracy_mercator.resources.mercator2.IMercatorProposal'
)


organisation_status_map = {
    'registered_nonprofit': 'non_profit',
    'planned_nonprofit': 'non_profit_planned',
    'support_needed': 'no_non_profit',
}


heard_froms_map = {
    'website': 'websites',
}


def translate_idea_topic(topics):
    return [t.replace('_and_', '_') for t in topics if t != 'other']


def parse_heard_froms(heard_froms):
    value = heard_froms[0]
    return heard_froms_map.get(value, value)


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
        ("title", "idea_subtitle")
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
             'partner_organisation_1_country'),
            ('partner2_name', 'partner_organisation_2_name'),
            ('partner2_website', 'partner_organisation_2_website'),
            ('partner2_country',
             'partner_organisation_2_country'),
            ('partner3_name', 'partner_organisation_3_name'),
            ('partner3_website', 'partner_organisation_3_website'),
            ('partner3_country',
             'partner_organisation_3_country'),
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


default_fields = [
    'importance',  # public
]


resources_are_versionable = False
