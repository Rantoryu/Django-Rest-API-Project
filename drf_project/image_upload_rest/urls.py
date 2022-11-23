from django.urls import include, path
from rest_framework import routers
from image_upload_rest.viewsets import UploadImageViewSet

router = routers.DefaultRouter()
router.register('images', UploadImageViewSet, 'images')
#router.register('thumbnail', UploadThumbnailViewSet, 'thumbnail')

urlpatterns = [
    path("", include(router.urls)),
]
