from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class UserProfile(models.Model):
    user_profile = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    profile_photo = CloudinaryField('image', default='placeholder')
    bio = models.TextField()
