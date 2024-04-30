from django.contrib.auth.models import User 
from django import forms


class EditAccountForm(forms.ModelForm):
    '''Form used for editing account'''
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
