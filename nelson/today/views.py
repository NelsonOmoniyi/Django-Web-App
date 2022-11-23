from django.shortcuts import render
import datetime

# Create your views here.
def today(request):
    now = datetime.datetime.now()
    return render(request, "today/index.html", {
        "today": now.month == 1 and now.day == 1
    })