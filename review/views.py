from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

from .models import BookReview, Comment
from .forms import CommentForm, ReviewForm

# Create your views here.


class BookReviewList(generic.ListView):
    queryset = BookReview.objects.filter(status=1)
    template_name = "review/index.html"
    paginate_by = 6


class AddReviewView(SuccessMessageMixin, generic.CreateView):
    model = BookReview
    template_name = 'review/add_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')
    success_message = 'Your review has been successfully pusblished.'

    def form_valid(self, form):
        if 'save_draft' in self.request.POST:
            self.instance = form.save(commit=False)
            # Assign current user as reviewer
            self.instance.reviewer = self.request.user
            # Create slug base format
            slug_format = f'''
{self.request.user.username}-{form.cleaned_data['book_title']}'''
            # Slugify reviewer's username and book title
            self.instance.slug = slugify(slug_format)
            self.instance.status = 0
            self.instance.save()
            self.success_message = 'Your review has been saved as draft.'
            return super().form_valid(form)
        else:
            self.instance = form.save(commit=False)
            # Assign current user as reviewer
            self.instance.reviewer = self.request.user
            # Create slug base format
            slug_format = f'''
{self.request.user.username}-{form.cleaned_data['book_title']}'''
            # Slugify reviewer's username and book title
            self.instance.slug = slugify(slug_format)
            self.instance.status = 1
            self.instance.save()
            return super().form_valid(form)


class DeleteReviewView(SuccessMessageMixin, generic.DeleteView):
    model = BookReview
    template_name = 'review/delete_review.html'
    success_url = reverse_lazy('home')
    success_message = 'Your review has been successfully deleted.'


class EditReviewView(SuccessMessageMixin, generic.UpdateView):
    model = BookReview
    template_name = 'review/edit_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.instance = form.save(commit=False)
        if 'publish' in self.request.POST:
            if self.instance.status == 0:
                self.instance.status = 1
                self.success_message = 'Your draft has been published.'
            else:
                self.success_message = 'Your review has been updated.'
        elif 'save_draft' in self.request.POST:
            self.instance.status = 0
            self.success_message = 'Your changes have been saved as draft.'
        slug_format = f'''
{self.request.user.username}-{form.cleaned_data['book_title']}'''
        self.instance.slug = slugify(slug_format)
        self.instance.save()
        return super().form_valid(form)


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


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """

    if request.method == "POST":
        queryset = BookReview.objects.filter(status=1)
        book_review = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment = comment_form.save(commit=False)
            comment.book_review = book_review
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Comment Updated!'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """

    queryset = BookReview.objects.filter(status=1)
    book_review = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))
