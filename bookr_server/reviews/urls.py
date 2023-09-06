from django.contrib import admin
from django.urls import path, include
from . import dash_proto
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("search", views.book_search, name="search"),
    path("list", views.book_list, name="list"),
    path("django_plotly_dash/", include("django_plotly_dash.urls")),
    path("dash", views.dash_proto, name="dash-proto"),
]
