import crispy_forms as crisp
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from apps.invites.models import IdeaInvite

from . import models
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

COLLABORATORS_EDIT_TITLE = _('Remove collaborators from your project.')
COLLABORATORS_EDIT_HELP = _('These people are now collaborating on your idea. '
                            'You can delete them here and they will not be '
                            'able to make changes to your idea anymore.')

INVITES_EDIT_TITLE = _('Revoke collaboration invites sent earlier.')
INVITES_EDIT_HELP = _('These email addresses have received invites to '
                      'collaborate but not accepted them yet. '
                      'You can delete them here and they will not be '
                      'able to join your project.')


class BaseForm(forms.ModelForm):
    @property
    def helper(self):
        helper = crisp.helper.FormHelper(self)
        helper.form_tag = False
        return helper


class ApplicantSectionForm(BaseForm):
    section_name = _('Applicant Section')

    class Meta:
        model = AbstractApplicantSection
        exclude = []


class PartnersSectionForm(BaseForm):
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
        helper = super().helper
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
        exclude = []


class ImpactSectionForm(BaseForm):
    section_name = _('Impact')

    class Meta:
        model = AbstractImpactSection
        exclude = []


class CollaborationCampSectionForm(BaseForm):
    section_name = _('Collaboration camp')

    class Meta:
        model = AbstractCollaborationCampSection
        exclude = []


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
        exclude = []


class FinanceAndDurationSectionForm(BaseForm):
    section_name = _('Finances and Duration')

    class Meta:
        model = AbstractFinanceAndDurationSection
        exclude = []


class IdeaSketchEditForm(BaseForm):

    class Meta:
        model = models.IdeaSketch
        exclude = [
            'collaborators_emails', 'how_did_you_hear', 'creator', 'module'
        ]


class CommunitySectionEditForm(CollaboratorsEmailsFormMixin, BaseForm):
    section_name = _('Community Information')
    collaborators_emails = forms.CharField(
        required=False,
        help_text=COLLABORATORS_HELP,
        label=COLLABORATORS_TITLE)

    class Meta:
        model = models.Idea
        fields = [
            'collaborators_emails',
            'reach_out',
            'how_did_you_hear',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            collaborators = self.collaborator_names
            if collaborators:
                self.fields['collaborators'] = forms.MultipleChoiceField(
                    required=False,
                    help_text=COLLABORATORS_EDIT_HELP,
                    label=COLLABORATORS_EDIT_TITLE,
                    choices=[
                        (c, c) for c in collaborators
                    ],
                    initial=collaborators,
                    widget=forms.CheckboxSelectMultiple
                )

            invites = self.invite_emails
            if invites:
                self.fields['invites'] = forms.MultipleChoiceField(
                    required=False,
                    help_text=INVITES_EDIT_HELP,
                    label=INVITES_EDIT_TITLE,
                    choices=[
                        (i, i) for i in invites
                    ],
                    initial=invites,
                    widget=forms.CheckboxSelectMultiple
                )
            self.fields.move_to_end('invites', last=False)
            self.fields.move_to_end('collaborators', last=False)
            self.fields.move_to_end('collaborators_emails', last=False)

    @property
    def helper(self):
        helper = super().helper
        helper['collaborators'].wrap(
            crisp.layout.Field,
            wrapper_class='checkboxes-delete',
            css_class='checkbox-delete'
        )
        helper['invites'].wrap(
            crisp.layout.Field,
            wrapper_class='checkboxes-delete',
            css_class='checkbox-delete'
        )
        return helper

    @property
    def collaborator_names(self):
        return self.instance.collaborators.all().values_list(
            'username', flat=True
        )

    @property
    def invite_emails(self):
        return self.instance.ideainvite_set.values_list('email', flat=True)

    def clean(self):
        super().clean()
        addresses = self.cleaned_data.get('collaborators_emails', [])
        invites = self.cleaned_data.get('invites', [])
        collaborators = self.cleaned_data.get('collaborators', [])

        duplicate_errors = []
        for (name, address) in addresses:
            if address in invites:
                error = ValidationError({
                   'collaborators_emails': _(
                       'You already invited {email}'
                   ).format(email=address)
                })
                duplicate_errors.append(error)
        if duplicate_errors:
            raise ValidationError(duplicate_errors)

        collaborator_count = sum([
            len(addresses),
            len(invites),
            len(collaborators),
        ])

        if collaborator_count > 5:
            raise ValidationError(_('Maximum 5 collaborators allowed'))

    def save(self):
        """
        Deletes invites and collaborators and adds new invites of instance.

        There is a little hack here, it uses the idea creator and not the
        current user as creator for the invites. There for no user needs to
        passed and it can be used in the edit view, just as all other forms.
        """

        collaborators = self.instance.collaborators.exclude(
            username__in=self.cleaned_data.get('collaborators', [])
        )
        self.instance.collaborators.remove(*collaborators)

        self.instance.ideainvite_set.exclude(
            email__in=self.cleaned_data.get('invites', [])
        ).delete()

        if 'collaborators_emails' in self.cleaned_data:
            for name, email in self.cleaned_data['collaborators_emails']:
                IdeaInvite.objects.invite(
                    self.instance.creator,
                    self.instance,
                    email
                )

        return self.instance
