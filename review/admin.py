from django.contrib import admin
from .models import BookReview, Comment

# Register your models here.

admin.site.register(BookReview)
admin.site.register(Comment)
