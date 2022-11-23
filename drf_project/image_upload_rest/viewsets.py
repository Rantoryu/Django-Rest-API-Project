from rest_framework import viewsets
from image_upload.models import UploadImage
from image_upload_rest.serializers import UploadImageSerializer


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer


# class UploadThumbnailViewSet(viewsets.ModelViewSet):
    #queryset = UploadImage.objects.values_list('thumbnail')
    #serializer_class = UploadImageSerializer
