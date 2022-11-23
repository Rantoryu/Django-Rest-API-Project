import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.


def gallery_view(request):
    path = settings.MEDIA_ROOT
    path_thumbnail = settings.THUMBNAIL_ROOT
    path_thumbnail_premium = settings.THUMBNAIL_PREMIUM_ROOT
    img_list = os.listdir(path)
    thumbnail_list = os.listdir(path_thumbnail)
    thumbnail_premium_list = os.listdir(path_thumbnail_premium)
    context = {"images": img_list, "thumbnails": thumbnail_list,
               "thumbnails_premium": thumbnail_premium_list}
    return render(request, 'index.html', context)


def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')
