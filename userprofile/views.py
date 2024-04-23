from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic

from review.models import BookReview
from .forms import EditAccountForm, CreateProfilePageForm
from .models import UserProfile

# Create your views here.


class EditAccountView(SuccessMessageMixin, generic.UpdateView):
	form_class = EditAccountForm
	template_name = 'userprofile/edit_account.html'
	success_url = reverse_lazy('home')
	success_message = 'Your account has been successfully updated.'

	def get_object(self):
		return self.request.user


class ProfilePageView(generic.DetailView):
	model = UserProfile
	template_name = 'userprofile/profile_page.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProfilePageView, self).get_context_data(
			*args, **kwargs
		)
		profile_page = get_object_or_404(UserProfile, id=self.kwargs['pk'])
		context['profile_page'] = profile_page
		context['user_reviews'] = BookReview.objects.filter(
			reviewer_id=self.kwargs['pk'],
			status=1
		)
		context['user_draft_reviews'] = BookReview.objects.filter(
			reviewer_id=self.kwargs['pk'],
			status=0
		)
		return context


class CreateProfilePageView(SuccessMessageMixin, generic.CreateView):
	model = UserProfile
	form_class = CreateProfilePageForm
	template_name = 'userprofile/create_profile_page.html'
	success_message = 'Your profile page has been successfully created.'

	def form_valid(self, form):
		form.instance.user_profile = self.request.user
		return super().form_valid(form)


class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
	model = UserProfile
	template_name = 'userprofile/edit_profile_page.html'
	fields = ['profile_photo', 'bio']
	success_url = reverse_lazy('home')
	success_message = 'Your profile page has been successfully updated.'
