from django.contrib import admin
from django.db import models

from . import models as idea_models


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
    exclude = ['module']
    raw_id_fields = ('creator', 'collaborators')
    search_fields = ('idea_title',)
    list_filter = (
        'module__project__name',
        'is_winner',
        'is_on_shortlist',
        'community_award_winner',
    )

    formfield_overrides = {
        models.TextField: {'max_length': None,
                           'help_text': None},
    }

    list_display = ['idea_title', 'type', 'is_on_shortlist',
                    'community_award_winner', 'is_winner', 'created']
    ordering = ['-created', 'idea_title']
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
                       'budget_granted',
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
                       in idea_models.AbstractApplicantSection
                       ._meta.get_fields()]),
        }),
        ('Partner Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractPartnersSection
                       ._meta.get_fields()]),
        }),
        ('Idea Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractIdeaSection
                       ._meta.get_fields()]),
        }),
        ('Impact Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractImpactSection
                       ._meta.get_fields()]),
        }),
        ('Community Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractCommunitySection
                       ._meta.get_fields()]),
        }),
    )


class IdeaSketchArchivedAdmin(admin.ModelAdmin):
    raw_id_fields = ('creator', 'collaborators')
    search_fields = ('idea_title',)

    formfield_overrides = {
        models.TextField: {'max_length': None,
                           'help_text': None},
    }

    fieldsets = (
        ('Creator and Collaborators', {
            'classes': ('collapse',),
            'fields': ('creator',
                       'collaborators')
        }),
        ('Applicant Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractApplicantSection
                       ._meta.get_fields()]),
        }),
        ('Partner Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractPartnersSection
                       ._meta.get_fields()]),
        }),
        ('Idea Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractIdeaSection
                       ._meta.get_fields()]),
        }),
        ('Impact Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractImpactSection
                       ._meta.get_fields()]),
        }),
        ('Community Section', {
            'classes': ('collapse',),
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractCommunitySection
                       ._meta.get_fields()]),
        }),
    )


class ProposalAdmin(admin.ModelAdmin):
    search_fields = ('idea_title',)

    formfield_overrides = {
        models.TextField: {'max_length': None,
                           'help_text': None},
    }

    fieldsets = (
        ('Finances and Duration', {
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractFinanceAndDurationSection
                       ._meta.get_fields()]),
        }),
        ('Selection', {
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractSelectionCriteriaSection
                       ._meta.get_fields()]),
        })
    )


class IdeaSketchAdmin(admin.ModelAdmin):
    search_fields = ('idea_title',)

    formfield_overrides = {
        models.TextField: {'max_length': None,
                           'help_text': None},
    }

    fieldsets = (
        ('Collaboration Camp', {
            'fields':
                tuple([field.name for field
                       in idea_models.AbstractCollaborationCampSection
                       ._meta.get_fields()]),
        }),
    )


admin.site.register(idea_models.Idea, IdeaAdmin)
admin.site.register(idea_models.IdeaSketchArchived, IdeaSketchArchivedAdmin)
admin.site.register(idea_models.Proposal, ProposalAdmin)
admin.site.register(idea_models.IdeaSketch, IdeaSketchAdmin)
