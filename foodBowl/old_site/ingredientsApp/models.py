from django.db import models


# Create your models here.
"""
define category

define recipe with 
directions
fat
categories
desc
protein
rating
title
ingredients+amnts
sodium
"""

class Category(models.Model):
    """
    Model class for a single category, which could be ingredient, festivity, typical meal type(e.g dinner)
    """
    name = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    """
    Model class for a single recipe
    """
    directions = models.TextField()
    fats = models.IntegerField(default=0, blank=True)
    categories = models.ManyToManyField('Category')
    calories = models.IntegerField(default=0, blank=True)
    desc = models.TextField(blank=True)
    protein = models.IntegerField(default=0, blank=True)
    name = models.TextField(default="Nameless")
    ingredDetails = models.TextField(default=None)
    sodium = models.IntegerField(default=0, blank=True)
    
    def __str(self):
        return self.name


