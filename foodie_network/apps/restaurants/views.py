from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import Restaurant, Review
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404
from .forms import ReviewForm


# Create your views here.
User = get_user_model()

# Create your views here.

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = 'restaurants/restaurant_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        context['reviews'] = Review.objects.filter(restaurant = restaurant)
        return context

class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    template_name = 'restaurants/restaurants_list.html'

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = 'restaurants/restaurant_form.html'
    fields = ('name', 'cover_pic', 'location', 'phone_number', 'rating')

@login_required
def add_review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk = pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.restaurant = restaurant
            review.writer = request.user
            review.save()
            return redirect('restaurants:restaurant_detail', pk = restaurant.pk)
    else:
        form = ReviewForm()
    return render(request, 'restaurants/review_form.html', {'form':form})
