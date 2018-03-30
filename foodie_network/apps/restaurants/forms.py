from django import forms
from .models import Review
from django.contrib.auth import get_user_model
User = get_user_model()



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
