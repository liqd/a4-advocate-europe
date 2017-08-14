from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from adhocracy4 import transforms

from adhocracy4.models.base import UserGeneratedContentModel

from apps.ideas.models import Idea

TEXT_HELPTEXT = _("To add videos from Vimeo, "
                  "Youtube or Facebook just paste the url "
                  "into the text.")


class JourneyEntry(UserGeneratedContentModel):
    IMPACT_ROAD = 'ir'
    HEROINES = 'he'
    IMPACT_STORY = 'is'
    IDEA = 'id'
    SUCCESS = 'su'
    FAILING = 'fa'
    JOIN = 'jo'
    ANYTHING = 'an'
    CATEGORY_CHOICES = (
        (IMPACT_ROAD, _('Road to impact')),
        (HEROINES, _('Heroines and heroes')),
        (IMPACT_STORY, _('Impact Story')),
        (IDEA, _('Take this idea!')),
        (SUCCESS, _('Success')),
        (FAILING, _('Failing forward')),
        (JOIN, _('Join forces!')),
        (ANYTHING, _('Anything else?'))
    )

    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES
    )
    text = RichTextUploadingField(config_name='image-editor',
                                  help_text=TEXT_HELPTEXT)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea-detail', args=[self.idea.slug])

    def save(self, *args, **kwargs):
        self.text = transforms.clean_html_field(
            self.text,
            setting='image-editor')
        super().save(*args, **kwargs)

    @property
    def project(self):
        return self.idea.project
