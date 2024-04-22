from django.urls import path
from . import views


urlpatterns = [
    path(
        'edit_account/',
        views.EditAccountView.as_view(),
        name='edit_account'
    ),
]
