from django.contrib import admin
from django.urls import path
from ethapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blocklookup', views.blocklookup, name='blocklookup'),
]
