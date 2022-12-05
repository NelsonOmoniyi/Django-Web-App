from django.urls import path
from . import views 

app_name = "tasks"
urlpatterns = [
    path("", views.task, name='task'),
    path("add", views.add, name='add')
]