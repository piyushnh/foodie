from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .forms import ProfileForm, UserForm
from .models import Profile


# Create your views here.
User = get_user_model()


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'userprofiles/profile.html'

#Function to update profile
@login_required
@transaction.atomic
def update_profile(request,pk):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Yay! You updated the details successfully!")
            return redirect('userprofiles:profile', pk=pk)
        else:
            for i in range(10):
                print('fuck')
            messages.error(request,("Please fix the errors!"))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = ProfileForm(instance = request.user.profile)

        return render(request, 'userprofiles/profile_form.html', {'user_form':user_form,
                                                                    'profile_form':profile_form})
