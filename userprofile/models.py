from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class UserProfile(models.Model):
    '''Stores a single user profile related to :model:`auth.User`'''
    user_profile = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    profile_photo = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user_profile)

    # Redirects back to home page
    def get_absolute_url(self):
        return reverse('home')
