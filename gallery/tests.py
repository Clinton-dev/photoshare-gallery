from django.test import TestCase

from .models import Category, Photo, Location

class PhotoTest(TestCase):
    def testfields(self):
        photo = Photo()
        photo.description = 'foo bar'
        photo.image = 'foobar.jpg'
        photo.save()

        record = Photo.objects.get(pk=1)
        self.assertAlmostEquals(record, photo)

class CategoryTest(TestCase):
    def testfields(self):
        category = Category()
        category.name = 'foo bar'
        category.save()

        record = Category.objects.get(pk=1)
        self.assertAlmostEquals(record, category)

class LocationTest(TestCase):
    def testfields(self):
        location = Location()
        location.name = 'foo bar'
        location.save()

        record = Location.objects.get(pk=1)
        self.assertAlmostEquals(record, location)