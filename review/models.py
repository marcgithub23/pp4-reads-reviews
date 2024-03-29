from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BookReview(models.Model):
    """
    Stores a single book review entry related to :model:`auth.User`
    """

    # Genre choices

    GENRE = [
        ("CLASSICS", "Classics"),
        ("CRIME", "Crime"),
        ("FANTASY", "Fantasy"),
        ("GENERAL_FICTION", "General Fiction"),
        ("HORROR", "Horror"),
        ("NONFICTION", "Nonfiction"),
        ("ROMANCE", "Romance"),
        ("SCIENCE_FICTION", "Science Fiction"),
        ("YOUNG_ADULT", "Young Adult")
    ]

    # Book rating choices

    BOOK_RATING = [
        ("ONE", 1),
        ("TWO", 2),
        ("THREE", 3),
        ("FOUR", 4),
        ("FIVE", 5)
    ]

    # Status choices

    STATUS = ((0, "Draft"), (1, "Published"))

    slug = models.SlugField(max_length=200, unique=True)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=50, choices=GENRE)
    book_blurb = models.TextField()
    book_rating = models.IntegerField(choices=BOOK_RATING)
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_reviews"
    )
    book_review = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
