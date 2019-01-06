from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^$', views.personal_first),
    url(r'^programming/$', views.programming),
    url(r'^construction/$', views.construction),
]