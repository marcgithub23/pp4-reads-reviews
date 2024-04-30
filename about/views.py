from django.contrib import messages
from django.shortcuts import render

from .forms import FeedbackForm
from .models import About

# Create your views here.


def about_website(request):
    """Renders the About page"""
    if request.method == "POST":
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Feedback received! Thank you for your support."
            )

    about = About.objects.all().order_by('-updated_on').first()
    feedback_form = FeedbackForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "feedback_form": feedback_form
        },
    )
