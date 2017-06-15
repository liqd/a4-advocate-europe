from django.contrib import admin

from . import models


admin.site.register(models.IdeaSketchArchived)
admin.site.register(models.Proposal)
admin.site.register(models.IdeaSketch)


def set_visit_camp_true(modeladmin, request, queryset):
    queryset.update(visit_camp=True)
set_visit_camp_true.short_description = 'Allow to add proposal'


def set_visit_camp_false(modeladmin, request, queryset):
    queryset.update(visit_camp=False)
set_visit_camp_false.short_description = 'Disallow to add proposal'


def set_community_award_winner_true(modeladmin, request, queryset):
    queryset.update(community_award_winner=True)
set_community_award_winner_true.\
    short_description = 'Set to community award winner'


def set_community_award_winner_false(modeladmin, request, queryset):
    queryset.update(community_award_winner=False)
set_community_award_winner_false.\
    short_description = 'Unset community award winner'


def set_is_winner_true(modeladmin, request, queryset):
    queryset.update(is_winner=True)
set_is_winner_true.short_description = 'Set to winner'


def set_is_winner_false(modeladmin, request, queryset):
    queryset.update(is_winner=False)
set_is_winner_false.short_description = 'Unset winner'


class IdeaAdmin(admin.ModelAdmin):
    list_display = ['idea_title', 'is_proposal', 'visit_camp',
                    'community_award_winner', 'is_winner']
    ordering = ['-is_proposal', '-visit_camp', '-is_winner', 'idea_title']
    actions = [
        set_visit_camp_true,
        set_visit_camp_false,
        set_community_award_winner_true,
        set_community_award_winner_false,
        set_is_winner_true,
        set_is_winner_false
    ]

admin.site.register(models.Idea, IdeaAdmin)
