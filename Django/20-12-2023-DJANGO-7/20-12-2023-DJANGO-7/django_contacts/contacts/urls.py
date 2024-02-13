
from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name="home"),
    path(route='add/', view=views.add, name="add"),
    path(route='admin/', view=views.admin, name="admin"),
    path(route='admin/add', view=views.add_user, name="add_user"),
    path(route='login/', view=views.login, name="login")
]
