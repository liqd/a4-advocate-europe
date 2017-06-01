from django.contrib import admin

from . import models


admin.site.register(models.IdeaSketchArchived)
admin.site.register(models.Proposal)
admin.site.register(models.Idea)


def set_visit_camp_true(modeladmin, request, queryset):
    queryset.update(visit_camp=True)
set_visit_camp_true.short_description = 'Allow to add proposal'


def set_visit_camp_false(modeladmin, request, queryset):
    queryset.update(visit_camp=False)
set_visit_camp_false.short_description = 'Disallow to add proposal'


class IdeaSketchAdmin(admin.ModelAdmin):
    list_display = ['idea_title', 'visit_camp']
    ordering = ['-visit_camp', 'idea_title']
    actions = [set_visit_camp_true, set_visit_camp_false]

admin.site.register(models.IdeaSketch, IdeaSketchAdmin)
