"""Managers for emencia.django.directory"""
from django.db import models

class ProfileManager(models.Manager):
    """Manager for the profiles"""
    
    def published(self):
        """Return all published profile"""
        return self.get_query_set().filter(visible=True)

                        
