from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookReviewList.as_view(), name='home'),
]
