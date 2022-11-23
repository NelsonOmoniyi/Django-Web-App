from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Hello"),
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.Brian, name="brian"),
    path("love", views.love, name="love")
]