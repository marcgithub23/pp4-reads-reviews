from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
]
