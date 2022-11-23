from django.core.exceptions import ValidationError


def validate_image_extension(value):
    value = str(value)
    if value.endswith(".jpg") != True and value.endswith(".png") != True:
        raise ValidationError(
            "Only images with JPG and PNG extension can be uploaded!")
    else:
        return value


def validate_image_size(image):
    file_size = image.size
    limit_mb = 4
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


def validator(image):
    error = False
    width = None
    height = None
    if width is not None and image.width > width:
        error = True
    if height is not None and image.height > height:
        error = True
    if error:
        raise ValidationError(
            [f'Size should not pass {width} x {height} pixels limit.']
        )
    return validator


def validate_maximum_size(width=None, height=None):
    return validator
