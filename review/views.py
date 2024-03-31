from django.shortcuts import render
from django.views import generic
from .models import BookReview

# Create your views here.


class BookReviewList(generic.ListView):
    queryset = BookReview.objects.all()
    template_name = "bookreview_list.html"
