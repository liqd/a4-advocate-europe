from django.contrib import admin, auth
from django.utils.translation import ugettext_lazy as _

from . import models


class UserAdmin(auth.admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Profile data'), {'fields': (
            '_avatar',
            'biographie',
            'europe',
            'twitter_handle',
            'facebook_handle',
            'instagram_handle',
            'website',
        )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined', 'last_login')
    list_display = (
        'username', 'email', 'date_joined', 'is_staff', 'is_superuser'
    )
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', 'email')


admin.site.register(models.User, UserAdmin)
