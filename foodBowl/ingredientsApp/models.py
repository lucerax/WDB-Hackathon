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
    name = models.TextField()
    categories = models.ManyToManyField('Category')
    directions = models.TextField()
    fats = models.FloatField()
    protein = models.FloatField()
    calories = models.FloatField()
    sodium = models.FloatField()
    desc = models.TextField(default=None)
    ingredDetails = models.TextField()


