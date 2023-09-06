from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("search", views.book_search, name="search"),
    path("list", views.book_list, name="list"),
]
