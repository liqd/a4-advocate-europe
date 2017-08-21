from django.contrib import admin

from . import models


admin.site.register(models.IdeaSketchArchived)
admin.site.register(models.Proposal)
admin.site.register(models.IdeaSketch)


def set_is_on_shortlist_true(modeladmin, request, queryset):
    queryset.update(is_on_shortlist=True)
set_is_on_shortlist_true.short_description = 'add to shortlist'


def set_is_on_shortlist_false(modeladmin, request, queryset):
    queryset.update(is_on_shortlist=False)
set_is_on_shortlist_false.short_description = 'remove from shortlist'


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
    raw_id_fields = ('collaborators',)
    exclude = ['module']
    readonly_fields = ['creator']
    list_display = ['idea_title', 'type', 'is_on_shortlist',
                    'community_award_winner', 'is_winner', 'created']
    ordering = ['-is_on_shortlist', '-is_winner', 'idea_title']
    actions = [
        set_is_on_shortlist_true,
        set_is_on_shortlist_false,
        set_community_award_winner_true,
        set_community_award_winner_false,
        set_is_winner_true,
        set_is_winner_false
    ]
    fieldsets = (
        ('Jury Section', {
            'fields': ('jury_statement',
                       ('is_on_shortlist',
                        'community_award_winner',
                        'is_winner')
                       )
        }),
        ('Creator and Collaborators', {
            'classes': ('collapse',),
            'fields': ('creator',
                       'collaborators')
        }),
        ('Applicant Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in models.AbstractApplicantSection._meta.get_fields()]),
        }),
        ('Partner Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in models.AbstractPartnersSection._meta.get_fields()]),
        }),
        ('Idea Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in models.AbstractIdeaSection._meta.get_fields()]),
        }),
        ('Impact Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in models.AbstractImpactSection._meta.get_fields()]),
        }),
        ('Community Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in models.AbstractCommunitySection._meta.get_fields()]),
        }),
    )
    list_filter = ('module__project',
                   'is_on_shortlist',
                   'community_award_winner',
                   'is_winner')
    search_fields = ['idea_title']

admin.site.register(models.Idea, IdeaAdmin)
