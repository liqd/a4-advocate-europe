from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        '^uploadimage',
        views.ImageUploadView.as_view(),
        name='upload_image',
    ),
]
