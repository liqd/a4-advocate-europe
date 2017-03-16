from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL', blank=True)
    twitter = models.CharField(
        max_length=255, help_text='Your twitter username, without the @', blank=True)
    flickr = models.URLField(
        help_text='Your flickr page URL', blank=True)
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL' , blank=True)