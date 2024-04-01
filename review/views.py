from django.shortcuts import render
from django.views import generic
from .models import BookReview

# Create your views here.


class BookReviewList(generic.ListView):
    queryset = BookReview.objects.filter(status=1)
    template_name = "review/index.html"
    paginate_by = 6
