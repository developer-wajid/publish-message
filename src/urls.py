from django.contrib import admin
from django.urls import path 
from src.account import UserLoginView


urlpatterns = [
    path('user-login/',UserLoginView.as_view() ),
]
