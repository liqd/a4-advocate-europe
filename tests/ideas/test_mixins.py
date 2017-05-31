import pytest

from django import forms
from django.http import Http404
from django.views import generic

from apps.ideas import mixins


@pytest.fixture
def test_edit_view():

    class NumberForm(forms.Form):
        number = forms.IntegerField()

    class StringForm(forms.Form):
        string = forms.CharField()

    class TestEditView(mixins.MultiFormEditMixin, generic.FormView):
        form_classes = [NumberForm, StringForm]
        template_name = 'base.html'

    return TestEditView


def test_access_forms(rf, test_edit_view):
    view = test_edit_view.as_view()
    form_classes = test_edit_view.form_classes

    response = view(rf.get('/form'))
    assert response.context_data['form'].__class__ == form_classes[0]

    response = view(rf.get('/form/0'), form_number='0')
    assert response.context_data['form'].__class__ == form_classes[0]

    response = view(rf.get('/form/1'), form_number='1')
    assert response.context_data['form'].__class__ == form_classes[1]

    with pytest.raises(Http404):
        view(rf.get('/form/2'), form_number='2')

    with pytest.raises(Http404):
        view(rf.get('/form/1'), form_number='-1')

    with pytest.raises(Http404):
        view(rf.get('/form/invalid'), form_number='invalid')


def test_submit_form_with_next(rf, test_edit_view):
    """
    - submit invalid data
    - submit correct data and goto to next form
    - submit correct data and stay on form
    """

    view = test_edit_view.as_view()
    form_classes = test_edit_view.form_classes

    data = {
        'next': '/form/1',
        'number': 'invalid_number'
    }
    response = view(rf.post('/form/0',  data))
    assert response.status_code == 200
    assert response.context_data['form'].errors
    assert response.context_data['form'].__class__ == form_classes[0]

    data = {
        'next': '/form/1',
        'number': '1'
    }
    response = view(rf.post('/form/0',  data))
    assert response.status_code == 302
    assert response['location'] == '/form/1'

    data = {
        'number': '1'
    }
    response = view(rf.post('/form/0',  data))
    assert response.status_code == 302
    assert response['location'] == '/form/0'


@pytest.mark.django_db
def test_module_mixin(rf, module):

    class TestView(mixins.ModuleMixin, generic.TemplateView):
        template_name = 'base.html'

    view = TestView.as_view()
    response = view(rf.get('/module/' + module.slug), slug=module.slug)
    assert response.context_data['view'].object == module
    assert response.context_data['view'].module == module

    view = TestView.as_view()

    with pytest.raises(Http404):
        view(rf.get('/module/invalid'), slug='invalid')
