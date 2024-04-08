from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BookReview

# Create your views here.


class BookReviewList(generic.ListView):
    queryset = BookReview.objects.filter(status=1)
    template_name = "review/index.html"
    paginate_by = 6


def review_detail(request, slug):
    """
    Display an individual :model:`review.BookReview`.

    **Context**

    ``review``
        An instance of :model:`review.BookReview`.

    **Template:**

    :template:`review/review_detail.html`
    """

    queryset = BookReview.objects.filter(status=1)
    book_review = get_object_or_404(queryset, slug=slug)
    comments = book_review.comments.all().order_by("-created_on")
    comment_count = book_review.comments.all().count()

    return render(
        request,
        "review/review_detail.html",
        {
            "review": book_review,
            "comments": comments,
            "comment_count": comment_count,
        },
    )
