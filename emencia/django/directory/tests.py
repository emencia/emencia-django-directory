"""Unit tests for emencia.django.directory"""
from django.test import TestCase

from emencia.django.directory.models import Country
from emencia.django.directory.models import Category
from emencia.django.directory.models import Profile

class ProfileTestCase(TestCase):
    """Tests for Profile model"""

    def setUp(self):
        self.country = Country.objects.create(name='France', slug='slug')

    def test_manager_published(self):
        Profile.objects.create(first_name='John', last_name='Kennedy',
                               email='jk@wh.com', country=self.country,
                               slug='john-kennedy-fr')
        Profile.objects.create(first_name='Robert', last_name='Kennedy',
                               email='rk@wh.com', country=self.country,
                               slug='robert-kennedy-fr',
                               visible=False)
        
        self.assertEquals(Profile.objects.all().count(), 2)
        self.assertEquals(Profile.objects.published().count(), 1)
        
