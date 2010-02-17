"""Backend for authentifiying with a Profile"""
from emencia.django.directory.models import Profile

class ProfileBackend:
    """Backend for authentifying a Profile"""

    def authenticate(self, username=None, password=None):
        try:
            profile = self.model.objects.get(username=username, is_activate=True)
            if profile.check_password(password):
                return profile
        except Profile.DoesNotExist:
            return None

    def get_user(self, profile_id):
        try:
            return Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist:
            return None
