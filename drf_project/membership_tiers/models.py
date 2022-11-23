from django.db import models
from django.conf import settings

# Create your models here.

MEMBERSHIP_CHOICES = (
    ('Enterprise', 'Enterprise'),
    ('Premium', 'Premium'),
    ('Basic', 'Basic')
)


class Membership(models.Model):
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES,
        default='Basic',
        max_length=30)
    #thumbnail_size_conf = models.ImageField.__sizeof__

    def __str__(self) -> str:
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.ForeignKey(
        Membership, on_delete=models.SET_NULL, null=True)
