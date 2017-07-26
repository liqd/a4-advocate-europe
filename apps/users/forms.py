import crispy_forms as crisp
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', '_avatar', 'motto',
                  'occupation', 'city', 'country',
                  'birthdate', 'languages', 'gender',
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
                'occupation',
                'motto',
                'languages',
                Div(
                    Field('city', wrapper_class='col-md-6'),
                    Field('country', wrapper_class='col-md-6'),
                    css_class="row",
                ),
                Div(
                    Field('birthdate', wrapper_class='col-md-6'),
                    Field('gender', wrapper_class='col-md-6'),
                    css_class="row",
                )
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
            )
        )
        return helper
