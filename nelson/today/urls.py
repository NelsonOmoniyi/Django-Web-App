from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.today, name="today"),
]