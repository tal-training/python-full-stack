
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('add/', view=views.add, name="add"),
    path('', view=views.home, name="home"),
]
