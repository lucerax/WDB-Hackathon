from django.db import models

# Create your models here.
# new
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recipes = models.CharField(max_length=500, blank=True, default = 'banana')

    def __str__(self):
    	return self.user.username 


class Recipe(models.Model):
    users = models.ManyToManyField(User)
    text = models.CharField(max_length=300)
    url = models.URLField(max_length=400)

    def __str__(self):
        return self.text


