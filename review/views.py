from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import BookReview
from .forms import CommentForm

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

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.book_review = book_review
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )

    comment_form = CommentForm()

    return render(
        request,
        "review/review_detail.html",
        {
            "review": book_review,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
