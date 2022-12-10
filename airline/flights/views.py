from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight, Airport
# Create your views here.

def flights(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
