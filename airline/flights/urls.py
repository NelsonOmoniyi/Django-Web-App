from django.urls import path
from . import views 

# app_name = "airline"

urlpatterns = [
    path("", views.flights, name='flights'),
    # path("add", views.add, name='add')
]
