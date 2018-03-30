from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    cover_pic = models.ImageField(upload_to = 'userprofiles/restaurant_pics',blank=False )
    location = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length = 10, blank=False)
    rating = models.DecimalField(max_digits=2, decimal_places = 1)
    website_url = models.URLField(max_length=100, default='')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
               return reverse("restaurants:restaurant_detail", kwargs = {'pk':self.pk})


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.restaurant)
