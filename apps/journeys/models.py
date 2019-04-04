from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _

from adhocracy4 import transforms
from apps.ideas.models import Idea

TEXT_HELPTEXT = _("To add content from Vimeo, "
                  "Youtube, Facebook, flickr, "
                  "soundcloud or instagram "
                  "just paste the url "
                  "into the text.")


class JourneyEntry(models.Model):
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

    created = models.DateTimeField(editable=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, editable=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

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
        if self.pk is not None:
            self.modified = timezone.now()
        self.text = transforms.clean_html_field(
            self.text,
            setting='image-editor')
        super().save(*args, **kwargs)

    @property
    def project(self):
        return self.idea.project
