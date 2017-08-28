from ckeditor_uploader import views as ck_views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.i18n import javascript_catalog
from rest_framework import routers
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from adhocracy4.api import routers as a4routers
from adhocracy4.comments.api import CommentViewSet
from adhocracy4.ratings.api import RatingViewSet
from adhocracy4.reports.api import ReportViewSet
from apps.ideas import urls as idea_urls
from apps.invites import urls as invite_urls
from apps.journeys import urls as journey_urls
from apps.users import urls as user_urls

from . import urls_accounts


js_info_dict = {
    'packages': ('adhocracy4.comments',),
}

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet, base_name='reports')

ct_router = a4routers.ContentTypeDefaultRouter()
ct_router.register(r'comments', CommentViewSet, base_name='comments')
ct_router.register(r'ratings', RatingViewSet, base_name='ratings')

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(ct_router.urls)),
    url(r'^upload/',
        login_required(ck_views.upload), name='ckeditor_upload'),
    url(r'^browse/',
        never_cache(login_required(ck_views.browse)), name='ckeditor_browse'),
]

urlpatterns += i18n_patterns(
    url(r'^accounts/', include('allauth.account.urls')),
    url(r'^accounts/social/', include('allauth.socialaccount.urls')),
    url(r'', include(user_urls)),
    url(r'^ideas/', include(idea_urls)),
    url(r'^invites/', include(invite_urls)),
    url(r'^journeys/', include(journey_urls)),
    url(r'^jsi18n/$', javascript_catalog,
        js_info_dict, name='javascript-catalog'),
    url(r'', include(wagtail_urls))
)

urlpatterns += [
    url(r'^accounts/', include(urls_accounts)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
