"""Managers for emencia.django.directory"""
from django.db import models

class ProfileManager(models.Manager):
    """Manager for the profiles"""

    def published(self):
        """Return all published profiles"""
        return self.get_query_set().filter(visible=True)


class CompanyManager(models.Manager):
    """Manager for the companies"""

    def published(self):
        """Return all published companies"""
        return self.get_query_set().filter(visible=True)

