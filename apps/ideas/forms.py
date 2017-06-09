from itertools import chain

import crispy_forms as crisp
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models.abstracts.applicant_section import AbstractApplicantSection
from .models.abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .models.abstracts.community_section import AbstractCommunitySection
from .models.abstracts.finances_duration_section import \
    AbstractFinanceAndDurationSection
from .models.abstracts.idea_section import AbstractIdeaSection
from .models.abstracts.impact_section import AbstractImpactSection
from .models.abstracts.partners_section import AbstractPartnersSection
from .models.abstracts.selection_criteria_section import \
    AbstractSelectionCriteriaSection

ACCEPT_CONDITIONS_LABEL = _('I hereby confirm and agree that '
                            'my idea will be public once'
                            ' published. I confirm that I have '
                            'the right to share the idea and '
                            'the visual material '
                            'used in this proposal.')

COLLABORATORS_TITLE = _('Please add your collaborators here.')
COLLABORATORS_HELP = _('Here you can insert the email addresses of up to 5 '
                       'collaborators. Each of the named collaborators will '
                       'receive an email inviting them to register on the '
                       'Advocate Europe website. After registering they will '
                       'appear with their user name on your idea page and '
                       'will be able to edit your idea. ')


class BaseForm(forms.ModelForm):
    @property
    def helper(self):
        helper = crisp.helper.FormHelper()
        helper.form_tag = False
        return helper


class ApplicantSectionForm(BaseForm):
    section_name = _('Applicant Section')

    class Meta:
        model = AbstractApplicantSection
        fields = [
            'first_name',
            'last_name',
            'organisation_status',
            'organisation_status_extra',
            'organisation_name',
            'organisation_website',
            'organisation_country',
            'organisation_city',
            'contact_email',
            'year_of_registration'
        ]


class PartnersSectionForm(BaseForm):
    section_name = _('Partners')
    accordions = [
        _('first partner organisation'),
        _('second partner organisation'),
        _('third partner organisation'),
    ]

    class Meta:
        model = AbstractPartnersSection
        fields = list(
            chain.from_iterable((
                'partner_organisation_{}_name'.format(index),
                'partner_organisation_{}_website'.format(index),
                'partner_organisation_{}_country'.format(index)
            ) for index in range(1, 4))
        )
        fields.append('partners_more_info')

    @property
    def helper(self):
        helper = crisp.helper.FormHelper()
        helper.form_tag = False
        helper.render_unmentioned_fields = True
        helper.layout = crisp.bootstrap.Accordion(
            *[
                crisp.bootstrap.AccordionGroup(
                    heading,
                    'partner_organisation_{}_name'.format(index),
                    'partner_organisation_{}_website'.format(index),
                    'partner_organisation_{}_country'.format(index)
                ) for index, heading in enumerate(self.accordions, 1)
            ]
        )
        return helper


class IdeaSectionForm(BaseForm):
    section_name = _('Idea details')

    class Meta:
        model = AbstractIdeaSection
        fields = [
            'idea_title',
            'idea_subtitle',
            'idea_pitch',
            'idea_image',
            'idea_topics',
            'idea_topics_other',
            'idea_location',
            'idea_location_specify',
            'idea_location_ruhr'
        ]


class ImpactSectionForm(BaseForm):
    section_name = _('Impact')

    class Meta:
        model = AbstractImpactSection
        fields = [
            'challenge',
            'outcome',
            'plan',
            'importance',
            'target_group',
            'members'
        ]


class CollaborationCampSectionForm(BaseForm):
    section_name = _('Collaboration camp')

    class Meta:
        model = AbstractCollaborationCampSection
        fields = [
            'collaboration_camp_option',
            'collaboration_camp_represent',
            'collaboration_camp_email',
            'collaboration_camp_benefit'
        ]


class CommunitySectionForm(BaseForm):
    section_name = _('Community Information')
    collaborators_emails = forms.CharField(
        required=False,
        help_text=COLLABORATORS_HELP,
        label=COLLABORATORS_TITLE)
    accept_conditions = forms.BooleanField(label=ACCEPT_CONDITIONS_LABEL)

    class Meta:
        model = AbstractCommunitySection
        fields = [
            'collaborators_emails',
            'reach_out',
            'how_did_you_hear',
            'accept_conditions'
        ]

    def clean_collaborators_emails(self):
        from email.utils import getaddresses
        import re

        value = self.cleaned_data['collaborators_emails'].strip(' ,')
        addresses = getaddresses([value])
        errors = []

        for name, address in addresses:
            if not re.match(r'^.+@[^@]+', address):
                errors.append(
                    ValidationError('{msg} ({addr})'.format(
                        msg=_('Invalid email address'),
                        addr=address
                    ))
                )

        if len(addresses) > 5:
            errors.append(
                ValidationError(_('Maximum 5 collaborators allowed'))
            )

        if errors:
            raise ValidationError(errors)

        return addresses


class SelectionCriteriaSectionForm(BaseForm):
    section_name = _('Selection Criteria')

    class Meta:
        model = AbstractSelectionCriteriaSection
        fields = [
            'selection_cohesion',
            'selection_apart',
            'selection_relevance',
        ]


class FinanceAndDurationSectionForm(BaseForm):
    section_name = _('Finances and Duration')

    class Meta:
        model = AbstractFinanceAndDurationSection
        fields = [
            'total_budget',
            'budget_requested',
            'major_expenses',
            'other_sources',
            'other_sources_secured',
            'duration'
        ]


class FinishForm(forms.Form):
    section_name = _('Finish')

    @property
    def helper(self):
        helper = crisp.helper.FormHelper()
        helper.form_tag = False
        return helper
