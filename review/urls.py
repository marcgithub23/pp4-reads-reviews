from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
]
