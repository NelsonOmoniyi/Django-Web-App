from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value="5", max_value="8")

# Create your views here.
tasks = []
def task(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "task/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:task"))
        else:
            return render(request, "task/add.html", {
                "form": form
            })


    return render(request, "task/add.html", {
        "form": NewTaskForm()
    })