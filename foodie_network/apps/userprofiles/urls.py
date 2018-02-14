from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'userprofiles'

urlpatterns = [
url(r'^details/(?P<pk>\d+)/$', views.ProfileView.as_view(), name = 'profile'),
url(r'^profileform/(?P<pk>\d+)/$', views.update_profile, name='profile_form'),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
