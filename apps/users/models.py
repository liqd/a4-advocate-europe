from django.contrib.auth import models as auth_models
from django.core import validators
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.templatetags.static import static
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.files import get_thumbnailer

from adhocracy4.images import fields
from apps.ideas.models import Idea

from . import USERNAME_INVALID_MESSAGE, USERNAME_REGEX


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=75,
        unique=True,
        help_text=_(
            'Required. 60 characters or fewer. Letters, digits, spaces and '
            '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                USERNAME_REGEX, USERNAME_INVALID_MESSAGE, 'invalid')],
        error_messages={
            'unique': _('A user with that username already exists.')}
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _('A user with that email address already exists.')}
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.')
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.')
    )

    _avatar = fields.ConfiguredImageField(
        'avatar',
        upload_to='users/images',
        blank=True,
        verbose_name=_('Profile picture'),
        help_text=_('The image should be at least 340 pixel '
                    'wide and 340 pixel high.')
    )

    date_joined = models.DateTimeField(
        editable=False,
        default=timezone.now
    )

    europe = models.TextField(
        blank=True,
        max_length=200,
        verbose_name=_('Your interest in Europe'),
        help_text=_('Why do you care about Europe? '
                    'Where do you try to make a change? '
                    '(max. 200 characters)')
    )

    twitter_handle = models.CharField(
        blank=True,
        max_length=15,
        verbose_name=_('Twitter name'),
    )

    facebook_handle = models.CharField(
        blank=True,
        max_length=50,
        verbose_name=_('Facebook name'),
    )

    instagram_handle = models.CharField(
        blank=True,
        max_length=30,
        verbose_name=_('Instagram name'),
    )

    website = models.URLField(
        blank=True,
        verbose_name=_('Website'),
        help_text=_('Plase add either https:// or http:// '
                    'to the front of your URL.')
    )

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def avatar(self):
        if self._avatar:
            return self._avatar

    @property
    def fallback_avatar(self):
        number = self.pk % 5
        return static('images/avatars/avatar-{0:02d}.svg'.format(number))

    @property
    def is_innovator(self):
        return Idea.objects.filter(
            Q(creator=self) |
            Q(co_workers=self)
        ).count() > 0

    def avatar_or_fallback_url(self):
        if self._avatar:
            return get_thumbnailer(self._avatar)['avatar'].url
        else:
            return self.fallback_avatar

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        full_name = '%s <%s>' % (self.username, self.email)
        return full_name.strip()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.username)])
