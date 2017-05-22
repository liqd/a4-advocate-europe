from django.contrib import admin

from . import models

admin.site.register(models.IdeaSketch)
admin.site.register(models.IdeaSketchArchived)
admin.site.register(models.Proposal)
admin.site.register(models.Idea)
