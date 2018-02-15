from django.conf.urls import url, include
from django.conf import settings
from . import views

app_name = 'search'

urlpatterns = [
 url(r'^user$',views.user_search, name='user_search'),
]
