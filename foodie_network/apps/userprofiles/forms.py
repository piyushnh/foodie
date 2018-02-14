from django import forms
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime

now = datetime.datetime.now()

def get_year():
    years = []
    presentyear = now.year - 130
    for i in range(131):
        years.append(presentyear)
        presentyear += 1
    return years

years = get_year()
class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years = years))
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'profile_pic')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
