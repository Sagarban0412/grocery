from django.urls import path
from . import views

urlpatterns = [
  # path('', views.member, name='member'),
  path('contact', views.contact, name='contactg'),
]