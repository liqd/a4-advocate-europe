from .helpers import download_file, floatstr_to_int, parse_year

# Subresources and sheets that still require a mapping:
#
# description subresource: (Your idea in detail) DESCRIPTION
# story subresource: WHAT IS THE STORY BEHIND YOUR IDEA?

project_url = 'https://frontend.advocate-europe.eu/api/mercator/'


proposal_ct = (
    'adhocracy_mercator.resources.mercator.IMercatorProposal'
)


organisation_status_map = {
    'registered_nonprofit': 'non_profit',
    'planned_nonprofit': 'non_profit_planned',
    'support_needed': 'no_non_profit',
}


subresource_map = {
    'adhocracy_mercator.resources.mercator.IOrganizationInfo': {
        "adhocracy_mercator.sheets.mercator.IOrganizationInfo": [
            ("status", "organisation_status", organisation_status_map),
            ("country", "organisation_country"),
            ("name", "organisation_name"),
            # ("help_request", "???"),
            ("status_other", "organisation_status_extra"),
            ("planned_date", "year_of_registration", parse_year),
            ("website", "organisation_website"),
        ],
    },
    "adhocracy_mercator.resources.mercator.ILocation": {
        "adhocracy_mercator.sheets.mercator.ILocation": [
            # "location_is_linked_to_ruhr": "idea_location_ruhr",
            ("location_specific_1", "idea_location_specify"),
            # "location_specific_2": "???",
            # "location_specific_3": "???"
            # "location_is_online": "false",
            # "location_is_specific": "true",
        ]
    },
    "adhocracy_mercator.resources.mercator.IFinance": {
        "adhocracy_mercator.sheets.mercator.IFinance": [
            ("budget", "total_budget", floatstr_to_int),
            ("requested_funding", "budget_requested", floatstr_to_int),
            # ("major_expenses", "major_expenses"),
            # ('grandted', '???')
        ],
    },
    'adhocracy_mercator.resources.mercator.IPartners': {
        # PLEASE LIST YOUR PARTNER ORGANISATIONS AND TEAM MEMBERS WITH THEIR
        # RELEVANT EXPERIENCES/SKILLS.
        'adhocracy_mercator.sheets.mercator.IPartners': [
            ('partners', 'partners_more_info'),
        ]
    },
    'adhocracy_mercator.resources.mercator.IOutcome': {
        # WHAT WOULD BE A SUCCESSFUL OUTCOME OF YOUR PROJECT OR INITIATIVE?
        # WHAT IS THE AIM YOU WANT TO REACH?
        'adhocracy_mercator.sheets.mercator.IOutcome': [
            ('outcome', 'outcome'),
        ]
    },
    'adhocracy_mercator.resources.mercator.IIntroduction': {
        # Proposal pitch
        'adhocracy_mercator.sheets.mercator.IIntroduction': [
            ('teaser', 'idea_pitch'),
            ('picture', 'idea_image', download_file)
        ]
    },
    'adhocracy_mercator.resources.mercator.IExperience': {
        # COMMUNITY – SHARED EXPERIENCES
        'adhocracy_mercator.sheets.mercator.IExperience': [
            ('experience', 'reach_out'),
        ]
    },
    'adhocracy_mercator.resources.mercator.ISteps': {
        # HOW DO YOU WANT TO GET THERE?
        'adhocracy_mercator.sheets.mercator.ISteps': [
            ('steps', 'plan'),
        ]
    },
    'adhocracy_mercator.resources.mercator.IValue': {
        # WHY DOES EUROPE NEED YOUR IDEA?
        'adhocracy_mercator.sheets.mercator.IValue': [
            ('value', 'challenge'),
        ]
    },
    'adhocracy_mercator.resources.mercator2.ITarget': {
        # WHO ARE YOU DOING IT FOR?
        'adhocracy_mercator.sheets.mercator2.ITarget': [
            ('target', 'target_group')
        ]
    },
    'adhocracy_mercator.resources.mercator2.IConnectionCohesion': {
        # HOW WILL YOUR PROJECT IDEA STRENGTHEN CONNECTION AND COHESION
        # IN EUROPE?
        'adhocracy_mercator.sheets.mercator2.IConnectionCohesion': [
            ('connection_cohesion', 'selection_cohesion')
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
    'target_group',  # public
    ('how_did_you_hear', 'other'),
    'members',
    'importance',  # public
    ('duration', 12),
    'major_expenses',  # public
    'selection_apart',  # public
    'selection_cohesion',  # public
    'selection_relevance',  # public
]


resources_are_versionable = True


sheet_map = {
    "adhocracy_mercator.sheets.mercator.IUserInfo": [
        ("personal_name", "first_name"),
        ("family_name", "last_name"),
    ],
    "adhocracy_core.sheets.title.ITitle": [
        ("title", "idea_title")
    ],
}
