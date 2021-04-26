from django.contrib import admin
from .models import UserProfile

# Register your models here.
from . import models

admin.site.register(UserProfile)