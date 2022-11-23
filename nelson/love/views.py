from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nelson(request):
    return HttpResponse("Nelson Just Got Home")