from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Form class for users to submit a feedback 
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Feedback
        fields = ('name', 'email', 'message')
