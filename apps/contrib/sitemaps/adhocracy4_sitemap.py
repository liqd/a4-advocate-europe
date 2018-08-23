from django.contrib.sitemaps import Sitemap
from apps.ideas.models import Idea


class Adhocracy4Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Idea.objects.all()

    def lastmod(self, obj):
        if obj.modified:
            return obj.modified
        return obj.created
