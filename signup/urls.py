from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='sign up'),
    path('login/', views.login, name='sign up'),
]
