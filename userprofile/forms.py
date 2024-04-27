from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User 
from django import forms

from .models import UserProfile


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
