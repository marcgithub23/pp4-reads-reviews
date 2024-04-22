from django.contrib import admin

from .models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin for the UserProfile model."""

    list_display = ('user_profile', 'profile_photo', 'bio')
