from itertools import chain
from zlib import adler32

import crispy_forms as crisp
from django import forms
from django.core.exceptions import ValidationError
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from cms.contrib import helpers

from . import models
from .models.abstracts import finances_duration_section
from .models.abstracts.applicant_section import AbstractApplicantSection
from .models.abstracts.community_section import AbstractCommunitySection
from .models.abstracts.idea_challenge_camp_section import \
    AbstractIdeaChallengeCampSection
from .models.abstracts.idea_section import AbstractIdeaSection
from .models.abstracts.impact_section import AbstractImpactSection
from .models.abstracts.network_section import AbstractNetworkSection
from .models.abstracts.partners_section import AbstractPartnersSection
from .models.abstracts.selection_criteria_section import \
    AbstractSelectionCriteriaSection

CONFIRM_PUBLICITY_LABEL = _('I hereby confirm and agree that '
                            'my idea will be public once published. '
                            'I confirm that I have the right to share '
                            'the idea and the visual material '
                            'used in this proposal.')
ACCEPT_CONDITIONS_LABEL = _('I hereby agree to the {}terms'
                            ' and conditions{} of the Advocate'
                            ' Europe idea challenge.')
CONFIRM_IDEA_CHALLENGE_CAMP_WITH_DATE = _('If selected, a representative of '
                                          'my project will commit to joining '
                                          'the Idea Challenge Camp '
                                          'from {} to {}.')
CONFIRM_IDEA_CHALLENGE_CAMP_WITHOUT_DATE = _('If selected, a representative '
                                             'of my project will commit '
                                             'to joining the Idea Challenge '
                                             'Camp at the end of April 2018.')

COWORKERS_TITLE = _('Please add your team members here.')
COWORKERS_HELP = _('Here you can insert the email addresses of '
                   'up to 5 team members. They will receive an email '
                   'inviting them to register on the Advocate '
                   'Europe website. After registering they '
                   'will appear with their user name on your idea '
                   'page and will be able to edit your idea. ')

COWORKERS_EDIT_TITLE = _('Your team members')

IDEA_CHALLENGE_CAMP_OPTION_LINK = _('More information about '
                                    'the {}Idea Challenge Camp{}. '
                                    '(max. 150 characters)')


class BaseForm(forms.ModelForm):
    do_not_call_in_templates = True  # important when reading section name

    @property
    def helper(self):
        helper = crisp.helper.FormHelper(self)
        helper.form_tag = False
        return helper


class CoWorkersEmailsFormMixin:
    def clean_co_workers_emails(self):
        from email.utils import getaddresses
        import re

        value = self.cleaned_data['co_workers_emails'].strip(' ,')
        addresses = getaddresses([value])
        valid_addresses = []
        errors = []

        for name, address in addresses:
            if not re.match(r'^.+@[^@]+', address):
                errors.append(
                    ValidationError('{msg} ({addr})'.format(
                        msg=_('Invalid email address'),
                        addr=address
                    ))
                )

            if address in valid_addresses:
                errors.append(
                    ValidationError('{msg} ({addr})'.format(
                        msg=_('Duplicate email address'),
                        addr=address
                    ))
                )
            else:
                valid_addresses.append(address)

        if errors:
            raise ValidationError(errors)

        return addresses


class ApplicantSectionForm(BaseForm):
    section_name = _('About You')

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

    def clean(self):
        cleaned_data = super().clean()
        organisation_status = cleaned_data.get('organisation_status')
        organisation_status_extra = cleaned_data.get(
            'organisation_status_extra')
        if organisation_status and organisation_status == 'other':
                if not organisation_status_extra:
                    self.add_error('organisation_status_extra',
                                   _("You selected 'other' as "
                                     "organisation status. "
                                     "Please provide more information "
                                     "about your current status."))

    def __init__(self, *args, **kwargs):
        if 'end_date' in kwargs:
            self.end_date = kwargs.pop('end_date')
        else:
            self.end_date = None
        super().__init__(*args, **kwargs)
        if self.end_date:
            self.section_description = _('Applications may be submitted, '
                                         'in English only, until {}. '
                                         'After publishing, '
                                         'you can continue to edit '
                                         'all the fields '
                                         'of your application right up to {}.'
                                         .format(self.end_date, self.end_date))


class PartnersSectionForm(BaseForm):
    section_name = _('Partners')
    section_description = _('Please share the names '
                            'of your partner organisations here. '
                            'If you do not have any partner '
                            'organisations, leave the fields empty. '
                            'You can update these fields any time '
                            'before the application deadline.')
    accordions = [
        _('Partner Organisation 1'),
        _('Partner Organisation 2'),
        _('Partner Organisation 3'),
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
    section_name = _('Idea')

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

    def clean(self):
        cleaned_data = super().clean()
        idea_location = cleaned_data.get('idea_location')
        idea_location_ruhr = cleaned_data.get('idea_location_ruhr')
        idea_location_specify = cleaned_data.get('idea_location_specify')

        if idea_location and 'ruhr_linkage' in idea_location:
            if not idea_location_ruhr:
                self.add_error('idea_location_ruhr',
                               _('You indicated that your idea '
                                 'links to the Ruhr area of Germany. '
                                 'Please specify.'))

        if idea_location and 'city' in idea_location:
            if not idea_location_specify:
                self.add_error('idea_location_specify',
                               _('You indicated that your idea '
                                 'will take place in a city, '
                                 'country and/or region. '
                                 'Please specify.'))


class ImpactSectionForm(BaseForm):
    section_name = _('Road to Impact')

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['challenge'].help_text = helpers.add_link_to_helptext(
            self.fields['challenge'].help_text,
            "annual_theme_help_page")


class IdeaChallengeCampSectionForm(BaseForm):
    section_name = _('Idea Challenge Camp')

    class Meta:
        model = AbstractIdeaChallengeCampSection
        fields = [
            'idea_challenge_camp_represent',
            'idea_challenge_camp_benefit'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if helpers.get_idea_challenge_camp_settings().description:
            self.section_description = \
                helpers.get_idea_challenge_camp_settings().description
        self.fields['idea_challenge_camp_represent'].help_text = \
            helpers.add_link_to_helptext(
            self.fields['idea_challenge_camp_represent'].help_text,
            "communication_camp_help_page", IDEA_CHALLENGE_CAMP_OPTION_LINK)


class CommunitySectionForm(CoWorkersEmailsFormMixin, BaseForm):
    section_name = _('Community')
    co_workers_emails = forms.CharField(
        required=False,
        help_text=COWORKERS_HELP,
        label=COWORKERS_TITLE)
    confirm_publicity = forms.BooleanField(label=CONFIRM_PUBLICITY_LABEL)
    accept_conditions = forms.BooleanField(label='')
    confirm_idea_challenge_camp = forms.BooleanField(
        label=CONFIRM_IDEA_CHALLENGE_CAMP_WITHOUT_DATE)

    def __init__(self, *args, **kwargs):
        self.display_idea_challenge_camp_section = \
            kwargs.pop('display_idea_challenge_camp_checkbox')
        super().__init__(*args, **kwargs)
        self.fields['accept_conditions'].label = helpers.add_link_to_helptext(
            self.fields['accept_conditions'].label, "terms_of_use_page",
            ACCEPT_CONDITIONS_LABEL)
        settings = helpers.get_idea_challenge_camp_settings()
        if settings.start_date and settings.end_date:
            self.fields['confirm_idea_challenge_camp'].label = \
                CONFIRM_IDEA_CHALLENGE_CAMP_WITH_DATE.format(
                    settings.start_date, settings.end_date)
        if not self.display_idea_challenge_camp_section:
            del self.fields['confirm_idea_challenge_camp']

    class Meta:
        model = AbstractCommunitySection
        fields = [
            'co_workers_emails',
            'reach_out',
            'how_did_you_hear',
            'accept_conditions'
        ]

    def clean_co_workers_emails(self):
        addresses = super().clean_co_workers_emails()

        if len(addresses) > 5:
            raise ValidationError(_('Maximum 5 team members allowed'))

        return addresses


class SelectionCriteriaSectionForm(BaseForm):
    section_name = _('Outreach and indicators')

    class Meta:
        model = AbstractSelectionCriteriaSection
        fields = [
            'selection_apart',
            'selection_advocating',
            'selection_key_indicators'
        ]


class NetworkForm(BaseForm):
    section_name = _('Network')

    class Meta:
        model = AbstractNetworkSection
        fields = [
            'network'
        ]


class FinanceAndDurationSectionForm(BaseForm):
    section_name = _('Finances')

    budget_requested = forms.IntegerField(
        max_value=50000,
        min_value=0,
        label=finances_duration_section.BUDGET_REQUESTED_TITLE,
        help_text=finances_duration_section.BUDGET_REQUESTED_HELP
    )
    total_budget = forms.IntegerField(
        min_value=0,
        label=finances_duration_section.TOTAL_BUDGET_TITLE,
        help_text=finances_duration_section.TOTAL_BUDGET_HELP
    )

    class Meta:
        model = finances_duration_section.AbstractFinanceAndDurationSection
        fields = [
            'total_budget',
            'budget_requested',
            'major_expenses',
            'duration'
        ]

    def clean(self):
        cleaned_data = super().clean()
        budget_requested = cleaned_data.get('budget_requested')
        total_budget = cleaned_data.get('total_budget')

        if budget_requested and total_budget:
            if budget_requested > total_budget:
                self.add_error('__all__', _("The requested budget can't be "
                                            "higher than the total budget"))


class CommunitySectionEditForm(CoWorkersEmailsFormMixin, BaseForm):
    section_name = _('Community')
    co_workers_emails = forms.CharField(
        required=False,
        help_text=COWORKERS_HELP,
        label=COWORKERS_TITLE)

    class Meta:
        model = models.Idea
        fields = [
            'co_workers_emails',
            'reach_out',
            'how_did_you_hear',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            invites = self.instance.ideainvite_set.all()
            co_workers = self.instance.co_workers.all()
            if invites or co_workers:
                self.fields['co_workers'] = forms.MultipleChoiceField(
                    required=False,
                    label=COWORKERS_EDIT_TITLE,
                    choices=[
                        (
                            'c:'+c.username,
                            {
                                'username': c.username,
                                'avatar': c.avatar_or_fallback_url,
                                'cta_checked': _('remove'),
                                'cta_unchecked': _('will be removed on save')
                            }
                        ) for c in co_workers
                        ] + [
                        (
                            'i:'+i.email,
                            {
                                'username': i.email,
                                'avatar': self.fallback_avatar(i.email),
                                'detail': _('Invitation pending'),
                                'cta_checked': _('remove'),
                                'cta_unchecked': _('will be removed on save')
                            }
                        ) for i in invites
                        ],
                    initial=['c:'+c.username for c in co_workers] +
                            ['i:'+i.email for i in invites],
                    widget=forms.CheckboxSelectMultiple
                )
                self.fields.move_to_end('co_workers', last=False)

            self.fields.move_to_end('co_workers_emails', last=False)

    @property
    def helper(self):
        helper = super().helper
        helper['co_workers'].wrap(
            crisp.layout.Field,
            template="bootstrap3/user_checkboxselectmultiple_field.html",
        )
        return helper

    def fallback_avatar(self, email):
        number = adler32(bytes(email, 'UTF-8')) % 5
        return static('images/avatars/avatar-{0:02d}.svg'.format(number))

    def clean(self):
        super().clean()

        addresses = self.cleaned_data.get('co_workers_emails', [])
        invites = []
        co_workers = []
        for entry in self.cleaned_data.get('co_workers', []):
            if entry[:2] == 'c:':
                co_workers.append(entry[2:])
            else:
                invites.append(entry[2:])
        self.cleaned_data['invites'] = invites
        self.cleaned_data['co_workers'] = co_workers

        duplicate_errors = []
        for (name, address) in addresses:
            if address in invites:
                error = ValidationError({
                    'co_workers_emails': _(
                        'You already invited {email}'
                    ).format(email=address)
                })
                duplicate_errors.append(error)
        if duplicate_errors:
            raise ValidationError(duplicate_errors)

        co_worker_count = sum([
            len(addresses),
            len(invites),
            len(co_workers),
        ])

        if co_worker_count > 5:
            raise ValidationError(_('Maximum 5 team members allowed'))

    def save(self, commit=True):
        """
        Deletes invites and co-workers and adds new invites of instance.
        There is a little hack here, it uses the idea creator and not the
        current user as creator for the invites. There for no user needs to
        passed and it can be used in the edit view, just as all other forms.
        """
        super().save(commit)

        co_workers = self.instance.co_workers.exclude(
            username__in=self.cleaned_data.get('co_workers', [])
        )
        self.instance.co_workers.remove(*co_workers)

        self.instance.ideainvite_set.exclude(
            email__in=self.cleaned_data.get('invites', [])
        ).delete()

        if 'co_workers_emails' in self.cleaned_data:
            for name, email in self.cleaned_data['co_workers_emails']:
                self.instance.ideainvite_set.invite(
                    self.instance.creator,
                    email
                )

        return self.instance


class FinishForm(forms.Form):
    section_name = _('Submit and publish')

    class Meta:
        model = models.IdeaSketch
        exclude = [
            'co_workers_emails', 'how_did_you_hear', 'creator', 'module'
        ]

    @property
    def helper(self):
        helper = crisp.helper.FormHelper()
        helper.form_tag = False
        return helper
