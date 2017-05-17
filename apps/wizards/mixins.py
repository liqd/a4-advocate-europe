from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from formtools.wizard.forms import ManagementForm


class CustomWizardMixin:
    """
    Modifications:

      - store the last form that already has been validated
    """

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
        from_current_mismatch = (
            form_current_step != self.steps.current and
            self.storage.current_step is not None
        )
        if from_current_mismatch:
            # form refreshed, change current step
            self.storage.current_step = form_current_step

        # get the form for the current step
        form = self.get_form(data=self.request.POST, files=self.request.FILES)

        # goto while storing but not validating (unsafe!)
        wizard_goto_step = self.request.POST.get('wizard_store_and_goto_step')
        if wizard_goto_step and wizard_goto_step in self.get_form_list():
            self.storage.set_step_data(self.steps.current,
                                       self.process_step(form))
            self.storage.set_step_files(self.steps.current,
                                        self.process_step_files(form))
            return self.render_goto_step(wizard_goto_step)

        # and try to validate
        if form.is_valid():
            # if the form is valid, store the cleaned data and files.
            self.storage.set_step_data(self.steps.current,
                                       self.process_step(form))
            self.storage.set_step_files(self.steps.current,
                                        self.process_step_files(form))
            self.max_validated = self.steps.current

            wizard_goto_step = self.request.POST.get(
                'wizard_validate_and_goto_step'
            )
            if wizard_goto_step and wizard_goto_step in self.get_form_list():
                return self.render_goto_step(wizard_goto_step)
            # check if the current step is the last step
            elif self.steps.current == self.steps.last:
                # no more steps, render done view
                return self.render_done(form, **kwargs)
            else:
                # proceed to the next step
                return self.render_next_step(form)
        return self.render(form)

    @property
    def max_validated(self):
        return self.storage.extra_data.get('max_validated_step')

    @max_validated.setter
    def max_validated(self, new_step):
        all_steps = self.steps.all
        new_index = all_steps.index(new_step)

        if self.max_validated:
            max_index = all_steps.index(self.max_validated)
        else:
            max_index = -1

        if new_index > max_index:
            self.storage.extra_data['max_validated_step'] = new_step
