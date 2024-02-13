from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/<str:course_name>/", views.students_in_course, name="students_in_course"),
    path("student/<int:student_id>/", views.get_name_by_id, name="get_name_by_id"),
    path("course/student/id/<int:student_id>/", views.get_course_by_student_id, name="get_course_by_student_id"),
    path("course/student/name/<str:student_name>/", views.get_course_by_student_name, name="get_course_by_student_name"),
    path("grades/", views.grades, name="grades"),
    path("python/", views.students, name="grades"),
]