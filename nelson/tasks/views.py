from django.shortcuts import render

# Create your views here.
tasks = ["Nelson", "Precious", "Love"]
def task(request):
    return render(request, "task/index.html", {
        "tasks": tasks
    })