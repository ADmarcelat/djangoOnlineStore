# Map our URLs to our views function

from django.urls import path
from . import views

# URL Configuration
# This URL configuration has to be imported in the main URL configuration in urls.py
urlpatterns = [
    path('hello/', views.say_hi)
]
