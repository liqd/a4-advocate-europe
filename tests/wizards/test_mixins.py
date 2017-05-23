import os
import pytest

from django import forms
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from formtools.wizard.views import CookieWizardView

from apps.wizards import mixins


@pytest.fixture
def test_wizard_view():

    class TestWizardView(mixins.CustomWizardMixin, CookieWizardView):
        file_storage = FileSystemStorage(
            location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))

        def done(self, form_list, **kwargs):
            return HttpResponse(status=204)

    class NumberForm(forms.Form):
        number = forms.IntegerField()

    class ChoiceForm(forms.Form):
        choice = forms.ChoiceField(choices=[('test', 'Label for test')])

    class StringForm(forms.Form):
        string = forms.CharField()

    return TestWizardView.as_view([NumberForm, ChoiceForm, StringForm])


@pytest.fixture
def view_client():
    from django.test.client import RequestFactory

    class ViewClient(RequestFactory):

        def _wrapper(self, method, view, *args, **kwargs):
            request = method('/dummy_path', *args, **kwargs)
            response = view(request)
            self.cookies = response.cookies
            return response

        def post(self, *args, **kwargs):
            return self._wrapper(super().post, *args, **kwargs)

        def get(self, *args, **kwargs):
            return self._wrapper(super().get, *args, **kwargs)

    return ViewClient()


def test_max_validated_is_always_correct(view_client, test_wizard_view):
    """
    Fill out a three step wizard and ensure that even if an earlier form
    is submitted max_validate is still showing the latest valid form.
    """
    view = test_wizard_view

    response = view_client.get(view)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '0'
    assert response.context_data['view'].max_validated is None

    data = {
        'test_wizard_view-current_step': '0',
        '0-number': 'not_a_number'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert len(response.context_data['form'].errors) == 1
    assert response.context_data['view'].max_validated is None

    data = {
        'test_wizard_view-current_step': '0',
        '0-number': '9000'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '1'
    assert response.context_data['view'].max_validated == '0'

    data = {
        'test_wizard_view-current_step': '0',
        '0-number': '9000'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '1'
    assert response.context_data['view'].max_validated == '0'

    data = {
        'test_wizard_view-current_step': '1',
        '1-choice': 'test'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '2'
    assert response.context_data['view'].max_validated == '1'

    data = {
        'test_wizard_view-current_step': '0',
        '0-number': 'test'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['form'].errors
    assert response.context_data['wizard']['steps'].current == '0'
    assert response.context_data['view'].max_validated == '1'


def test_max_stored(view_client, test_wizard_view):
    """
    Submit first wizard form correctly moving max_stored to first form and
    on second form store and go back to second form moving max_stored to
    second form.
    """
    view = test_wizard_view

    response = view_client.get(view)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '0'
    assert response.context_data['view'].max_stored is None

    data = {
        'test_wizard_view-current_step': '0',
        '0-number': '42'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert len(response.context_data['form'].errors) == 1
    assert response.context_data['view'].max_stored is '0'

    data = {
        'wizard_store_and_goto_step': '0',
        'test_wizard_view-current_step': '1',
        '1-choice': 'invalid choice'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '0'
    assert response.context_data['view'].max_stored == '1'


def test_store_and_goto(view_client, test_wizard_view):
    """
    Store and validate first step and afterwards only store second
    step while going back to first step.
    """
    view = test_wizard_view

    data = {
        'test_wizard_view-current_step': '0',
        '0-number': '9000'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '1'

    data = {
        'wizard_store_and_goto_step': '0',
        'test_wizard_view-current_step': '1',
        '1-choice': 'invalid option',
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '0'
    storage = response.context_data['view'].storage
    assert '1-choice' in storage.get_step_data('1')
    assert storage.get_step_data('1')['1-choice'] == 'invalid option'


def test_validate_and_goto(view_client, test_wizard_view):
    """
    Store and validate first step and afterwards store and do the same
    for second step.
    """
    view = test_wizard_view

    data = {
        'test_wizard_view-current_step': '0',
        '0-number': '9000'
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '1'

    data = {
        'wizard_validate_and_goto_step': '0',
        'test_wizard_view-current_step': '1',
        '1-choice': 'invalid option',
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '1'
    assert response.context_data['form'].errors

    data = {
        'wizard_validate_and_goto_step': '0',
        'test_wizard_view-current_step': '1',
        '1-choice': 'test',
    }
    response = view_client.post(view, data)
    assert response.status_code == 200
    assert response.context_data['wizard']['steps'].current == '0'
    storage = response.context_data['view'].storage
    assert '1-choice' in storage.get_step_data('1')
    assert storage.get_step_data('1')['1-choice'] == 'test'
