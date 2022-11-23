import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from .validators import validate_image_extension, validate_maximum_size, validate_image_size
from django_resized import ResizedImageField
from membership_tiers.models import Membership


# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(verbose_name='Uploaded image', validators=[
                              validate_image_extension, validate_maximum_size(width=1920, height=1080), validate_image_size])  # type: ignore
    thumbnail = models.ImageField(
        upload_to='thumbnails', editable=False, blank=True, null=True)
    thumbnail_premium = models.ImageField(
        upload_to='thumbnails_premium', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            raise Exception(
                'Could not create thumbnail - is the file type valid?')

        super(UploadImage, self).save(*args, **kwargs)

    def make_thumbnail(self):

        image = Image.open(self.image)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension
        thumb_premium_filename = thumb_name + '_thumb_premium' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False

        temp_thumb_premium = BytesIO()
        temp_thumb = BytesIO()

        if Membership.membership_type == "Enterprise" or "Premium":
            new_height = 400
            new_width = int(new_height / image.height * image.width)
            image = image.resize((new_width, new_height))
            image.save(temp_thumb, FTYPE)
            new_height = 200
            new_width = int(new_height / image.height * image.width)
            image = image.resize((new_width, new_height))
            image.save(temp_thumb_premium, FTYPE)
        elif Membership.membership_type == "Basic":
            new_height = 200
            new_width = int(new_height / image.height * image.width)
            image = image.resize((new_width, new_height))
            image.save(temp_thumb, FTYPE)
        else:
            raise Exception("User has no membership")

        image.save(temp_thumb_premium, FTYPE)
        image.save(temp_thumb, FTYPE)

        temp_thumb_premium.seek(0)
        temp_thumb.seek(0)

        if Membership.membership_type == "Enterprise" or "Premium":
            self.thumbnail.save(thumb_filename, ContentFile(
                temp_thumb_premium.read()), save=False)
            self.thumbnail_premium.save(thumb_premium_filename, ContentFile(
                temp_thumb.read()), save=False)
        elif Membership.membership_type == "Basic":
            self.thumbnail.save(thumb_filename, ContentFile(
                temp_thumb.read()), save=False)
        else:
            raise Exception("User has no membership")
        temp_thumb.close()
        return True
