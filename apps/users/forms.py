import crispy_forms as crisp
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from django.utils.translation import ugettext_lazy as _
from cms.contrib import helpers

from .models import User

TERMS_OF_USE_LABEL = _('I accept the terms of use.')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', '_avatar', 'biographie', 'europe',
                  'twitter_handle', 'facebook_handle',
                  'instagram_handle', 'website', 'get_notifications']

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
                'biographie',
                'europe'
            ),
            Fieldset(
                _('Social Media Handlers'),
                Div(
                    Field('twitter_handle', wrapper_class='col-md-6'),
                    Field('facebook_handle', wrapper_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Field('instagram_handle', wrapper_class='col-md-6'),
                    Field('website', wrapper_class='col-md-6'),
                    css_class='row'
                )
            ),
            Fieldset(
                _('Notifications'),
                'get_notifications'
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
