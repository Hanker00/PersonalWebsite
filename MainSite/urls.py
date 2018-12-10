from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.personal_first),
    url(r'^programming/$', login, {'template_name': 'MainSite/programming.html'}),
]