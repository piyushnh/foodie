from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Profile

# Create your views here.


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'userprofiles/profile.html'

class CreateProfileView(LoginRequiredMixin, CreateView):
        model = Profile
        form = ProfileForm
        fields = ('date_of_birth', 'profile_pic')
        template_name = 'userprofiles/profile_form.html'
        success_url = reverse_lazy('userprofiles:profile')
