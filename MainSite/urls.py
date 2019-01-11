from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.personal_first, name='personal_first'),
    path('programming/', views.programming, name='programming'),
    path('construction/', views.construction, name='construction'),
]