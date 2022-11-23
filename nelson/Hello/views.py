from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def Brian(request):
    return HttpResponse("Hello Brian!")

def love(request):
    return HttpResponse("Love Me Say")

def greet(request, name):
    return render(request, "welcome/welcome.html", {
        "name": name.capitalize()
    })