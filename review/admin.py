from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BookReview, Comment


@admin.register(BookReview)
class BookReviewAdmin(SummernoteModelAdmin):

    list_display = ('book_title', 'slug', 'status')
    search_fields = ['book_title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('reviewer','book_title',)}
    summernote_fields = ('book_review',)


# Register your models here.

admin.site.register(Comment)
