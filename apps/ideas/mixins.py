from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.views import generic
from formtools.wizard.forms import ManagementForm

from adhocracy4.modules.models import Module


class ModuleMixin(generic.detail.SingleObjectMixin):
    model = Module

    def dispatch(self, request, *args, **kwargs):
        self.module = self.get_object()
        self.object = self.module
        return super().dispatch(request, *args, **kwargs)


class CustomWizardMixin:

    key = '__max_step_index__'

    def update_last_validated(self, form_current_step):
        max_step_index_dict = self.storage.get_step_data(self.key)
        max_step_index = None
        if max_step_index_dict:
            max_step_index = max_step_index_dict['x']
        current_step_index = self.steps.all.index(form_current_step)
        print(current_step_index)
        print(max_step_index)
        if max_step_index is None or current_step_index > max_step_index:
            self.storage.set_step_data(self.key, {'x': [current_step_index]})

    # def get_max_validated(self):

    def post(self, *args, **kwargs):
        """
        This method handles POST requests.
        The wizard will render either the current step (if form validation
        wasn't successful), the next step (if the current step was stored
        successful) or the done view (if no more steps are available)
        """

        # Check if form was refreshed
        management_form = ManagementForm(self.request.POST, prefix=self.prefix)
        if not management_form.is_valid():
            raise ValidationError(
                _('ManagementForm data is missing or has been tampered.'),
                code='missing_management_form',
            )

        form_current_step = management_form.cleaned_data['current_step']
        if (form_current_step != self.steps.current and
                self.storage.current_step is not None):
            # form refreshed, change current step
            self.storage.current_step = form_current_step

        # get the form for the current step
        form = self.get_form(data=self.request.POST, files=self.request.FILES)

        # and try to validate
        if form.is_valid():
            # if the form is valid, store the cleaned data and files.
            self.storage.set_step_data(self.steps.current,
                                       self.process_step(form))
            self.storage.set_step_files(self.steps.current,
                                        self.process_step_files(form))
            self.update_last_validated(form_current_step)

            # check if the current step is the last step
            if self.steps.current == self.steps.last:
                # no more steps, render done view
                return self.render_done(form, **kwargs)
            else:
                # proceed to the next step
                return self.render_next_step(form)
        return self.render(form)
