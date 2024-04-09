from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Feedback

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
