from django.contrib import admin
from django.urls import include, path

from my_app import views

urlpatterns = [
    path('login/', views.login, name='home'),
    path('patients/', views.patients, name='patients'),
]

