from django.conf.urls import url, include
app_name = 'custom_account'
urlpatterns = [
    url(r'^$', include('allauth.urls'), name='accounts'),
]
