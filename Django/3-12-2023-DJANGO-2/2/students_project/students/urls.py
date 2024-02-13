from django.urls import path

from . import views

urlpatterns = [
    path("", views.students, name="students"),
    path("courses/", views.courses, name="courses"),
    path("grades/", views.grades, name="grades"),
    path("python/", views.students, name="grades"),
]