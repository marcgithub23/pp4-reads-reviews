from django.urls import path
from . import views


urlpatterns = [
    path(
        'edit_account/',
        views.EditAccountView.as_view(),
        name='edit_account'
    ),
    path(
        'profile/<int:pk>',
        views.ProfilePageView.as_view(),
        name='profile_page'),
]
