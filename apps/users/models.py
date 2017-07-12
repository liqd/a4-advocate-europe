from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_countries import fields as countries_fields

from adhocracy4.images import fields

from . import USERNAME_INVALID_MESSAGE, USERNAME_REGEX


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=60,
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
        verbose_name=_('Avatar picture'),
    )

    date_joined = models.DateTimeField(
        editable=False,
        default=timezone.now
    )

    city = models.CharField(
        blank=True,
        max_length=80,
        verbose_name=_('City of residence'),
    )

    country = countries_fields.CountryField(
        blank=True,
        verbose_name=_('Country of residence'),
    )

    birthdate = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Date of birth'),
    )

    occupation = models.CharField(
        blank=True,
        max_length=80,
        verbose_name=_('Occupation')
    )

    languages = models.CharField(
        blank=True,
        verbose_name=_('Languages'),
        max_length=150,
        help_text=_('Enter the languages you’re speaking.')
    )

    motto = models.TextField(
        blank=True,
        verbose_name=_('Your motto of life'),
        help_text=_('Write a little bit about yourself. '
                    '(max. 250 characters)')
    )

    gender = models.CharField(
        blank=True,
        verbose_name=_('Gender'),
        max_length=2,
        choices=[
            ('M', _('Male')),
            ('F', _('Female')),
            ('T', _('Transgender')),
            ('TF', _('Transgender Female')),
            ('TM', _('Transgender Male')),
            ('I', _('Intersex')),
            ('GF', _('Gender Fluid')),
            ('O', _('Other')),
        ],
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
        verbose_name=_('Website')
    )

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def avatar(self):
        if self._avatar:
            return self._avatar

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        full_name = '%s <%s>' % (self.username, self.email)
        return full_name.strip()
