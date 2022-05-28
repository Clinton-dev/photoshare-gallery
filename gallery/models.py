from operator import mod
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=180, null=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL)


    def __str__(self):
        return self.description