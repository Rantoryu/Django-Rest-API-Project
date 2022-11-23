from django.contrib import admin
from .models import Membership, UserMembership

# Register your models here.
admin.site.register(Membership)
admin.site.register(UserMembership)
