from django.apps import AppConfig
from django.db.models.signals import post_save


class UserprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userprofile'

    def ready(self):
        from django.contrib.auth.models import User
        from userprofile.signals import create_profile, save_profile
        post_save.connect(create_profile, sender=User)
        post_save.connect(save_profile, sender=User)
