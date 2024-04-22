from django import forms
from .models import BookReview, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = (
            'book_cover',
            'book_title',
            'book_author',
            'book_genre',
            'book_blurb',
            'book_rating',
            'book_review',
            'status'
        )
        widgets = {
            'book_cover': forms.FileInput(
                attrs={'class':'form-control', 'type':'file'}),
            'book_title': forms.TextInput(attrs={'class':'form-control'}),
            'book_author': forms.TextInput(attrs={'class':'form-control'}),
            'book_genre': forms.Select(attrs={'class':'form-control'}),
            'book_blurb': forms.Textarea(attrs={'class':'form-control'}),
            'book_rating': forms.Select(attrs={'class':'form-control'}),
            'book_review': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }
