from django.contrib import admin

from .models import JourneyEntry


class JourneyEntryAdmin(admin.ModelAdmin):
    raw_id_fields = ('creator', 'idea')


admin.site.register(JourneyEntry, JourneyEntryAdmin)
