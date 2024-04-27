from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Create your models here.

class UserProfile(models.Model):
    user_profile = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    profile_photo = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user_profile)
    
    def get_absolute_url(self):
        return reverse('home')
