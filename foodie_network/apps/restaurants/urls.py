from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'restaurants'

urlpatterns = [
url(r'^details/(?P<pk>\d+)/$', views.RestaurantDetailView.as_view(), name = 'restaurant_detail'),
url(r'^new/$', views.RestaurantCreateView.as_view(), name = 'new_restaurant'),
url(r'^restaurant/(?P<pk>\d+)/review$', views.add_review, name='add_review'),
]
