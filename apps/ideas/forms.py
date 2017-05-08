import crispy_forms as crisp
from django.forms import BooleanField, ModelForm
from django.utils.translation import ugettext as _

from .models.abstracts.applicant_section import AbstractApplicantSection
from .models.abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .models.abstracts.community_section import AbstractCommunitySection
from .models.abstracts.finances_section import AbstractFinanceSection
from .models.abstracts.idea_section import AbstractIdeaSection
from .models.abstracts.impact_section import AbstractImpactSection
from .models.abstracts.partners_section import AbstractPartnersSection

ACCEPT_CONDITIONS_LABEL = _('I hereby confirm and agree that '
                            'my idea will be public once'
                            ' published. I confirm that I have '
                            'the right to share the idea and '
                            'the visual material '
                            'used in this proposal.')


class BaseForm(ModelForm):
    @property
    def helper(self):
        helper = crisp.helper.FormHelper()
        helper.form_tag = False
        return helper


class ApplicantSectionForm(BaseForm):
    section_name = _('Applicant Section')

    class Meta:
        model = AbstractApplicantSection
        exclude = []


class PartnersSectionForm(ModelForm):
    section_name = _('Partners')
    accordions = [
        _('first partner organisation'),
        _('second partner organisation'),
        _('third partner organisation'),
    ]

    class Meta:
        model = AbstractPartnersSection
        exclude = []

    @property
    def helper(self):
        helper = crisp.helper.FormHelper()
        helper.form_tag = False
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
        exclude = []


class ImpactSectionForm(BaseForm):
    section_name = _('Impact')

    class Meta:
        model = AbstractImpactSection
        exclude = []


class CollaborationCampSectionForm(BaseForm):
    section_name = _('Collaboration Camp')

    class Meta:
        model = AbstractCollaborationCampSection
        exclude = []


class CommunitySectionForm(BaseForm):
    section_name = _('Community Information')
    accept_conditions = BooleanField(label=ACCEPT_CONDITIONS_LABEL)

    class Meta:
        model = AbstractCommunitySection
        exclude = []


class FinanceSectionForm(BaseForm):
    section_name = _('Finances')

    class Meta:
        model = AbstractFinanceSection
        exclude = []
