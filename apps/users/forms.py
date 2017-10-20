import crispy_forms as crisp
from crispy_forms.layout import HTML, Div, Field, Fieldset, Layout, Submit
from django import forms
from django.utils.translation import ugettext_lazy as _
from cms.contrib import helpers

from .models import User

TERMS_OF_USE_LABEL = _('I accept the terms of use.')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', '_avatar', 'europe',
                  'twitter_handle', 'facebook_handle',
                  'instagram_handle', 'website']

    @property
    def helper(self):
        helper = crisp.helper.FormHelper(self)
        helper.form_class = 'custom-form'
        helper.add_input(Submit('submit', 'Submit'))
        helper.layout = Layout(
            Fieldset(
                _('Your Profile'),
                'username',
                '_avatar',
                'europe'
            ),
            Fieldset(
                _('Social Media'),
                Div(
                    Field('twitter_handle', wrapper_class='col-md-6'),
                    Field('facebook_handle', wrapper_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Field('instagram_handle', wrapper_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Field('website', wrapper_class='col-md-12'),
                    css_class='row'
                )
            )
        )
        return helper


class NotificationsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['get_notifications']

    @property
    def helper(self):
        helper = crisp.helper.FormHelper(self)
        helper.form_class = 'custom-form'
        helper.add_input(Submit('save', 'Save'))
        helper.layout = Layout(
            Fieldset(
                _('Notifications'),
                Div(
                    HTML("<p>I want to receive mails with notifications "
                         "about:</p>"),
                    Field('get_notifications'),
                    css_class='notification-settings'
                ),
            )
        )
        return helper


class SignUpForm(forms.Form):
    terms_of_use = forms.BooleanField(label=TERMS_OF_USE_LABEL)

    def signup(self, request, user):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['terms_of_use'].label = helpers.add_link_to_helptext(
            self.fields['terms_of_use'].label, "terms_of_use_page")
