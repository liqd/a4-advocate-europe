from django.forms import ModelForm

from .models.abstracts.applicant_section import AbstractApplicantSection
from .models.abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .models.abstracts.community_section import AbstractCommunitySection
from .models.abstracts.finances_section import AbstractFinanceSection
from .models.abstracts.idea_section import AbstractIdeaSection
from .models.abstracts.impact_section import AbstractImpactSection
from .models.abstracts.partners_section import AbstractPartnersSection


class ApplicantSectionForm(ModelForm):
    class Meta:
        model = AbstractApplicantSection
        exclude = []


class PartnersSectionForm(ModelForm):
    class Meta:
        model = AbstractPartnersSection
        exclude = []


class IdeaSectionForm(ModelForm):
    class Meta:
        model = AbstractIdeaSection
        exclude = []


class ImpactSectionForm(ModelForm):
    class Meta:
        model = AbstractImpactSection
        exclude = []


class CollaborationCampSectionForm(ModelForm):
    class Meta:
        model = AbstractCollaborationCampSection
        exclude = []


class CommunitySectionForm(ModelForm):
    class Meta:
        model = AbstractCommunitySection
        exclude = []


class FinanceSectionForm(ModelForm):
    class Meta:
        model = AbstractFinanceSection
        exclude = []
