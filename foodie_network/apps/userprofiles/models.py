from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

User = get_user_model()
#signal handling
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=True, null = True)
    #not sure of this null = true
    profile_pic = models.ImageField(upload_to = 'userprofiles/profile_pics',blank = True, null=True )
    display_status = models.TextField(default="Hey there! Welcome to my profile!")

    # def get_absolute_url(self):
    #     return reverse('userprofiles:profile_info', kwargs={'id':self.pk})

    def __str__(self):
        return str(self.user.first_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
