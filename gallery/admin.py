from django.contrib import admin

from .models import Category, Location, Photo
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Location)