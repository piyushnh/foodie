from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=,models.CASCADE)
    name = models.CharField(max_length = 100)
    restaurant_pic = models.ImageField(upload_to = 'userprofiles/restaurant_pics',blank=False )
    location = models.CharField(max_length=200, required=True)
    phone_number = models.CharField(max_length = 10, required=True)


    def __str__(self):
        return self.name
