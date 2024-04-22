from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic

from .forms import EditAccountForm
from .models import UserProfile

# Create your views here.


class EditAccountView(SuccessMessageMixin, generic.UpdateView):
	form_class = EditAccountForm
	template_name = 'userprofile/edit_account.html'
	success_url = reverse_lazy('home')
	success_message = 'Your account has been successfully updated.'

	def get_object(self):
		return self.request.user
