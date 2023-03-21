from django.contrib import admin
from django.urls import path, include  # add this
from .views import homeView

urlpatterns = [
    path("", homeView, name = 'home')
]