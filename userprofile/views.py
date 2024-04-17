from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from .models import UserProfile

# Create your views here.


def profile_page(request, user_id):
    """Display profile page of a user"""

    queryset = UserProfile.objects.filter()

    return render(
        request,
        ""
    )
