from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def edit(request, pk):  # we are going to pass a parameter in the request specifying the todo
    taskToUpdate = Task.objects.get(id=pk)
    form = TaskForm(instance=taskToUpdate)
    context = {'form': form}
    if request.method == "POST":
        form = TaskForm(request.POST, instance=taskToUpdate)
        if form.is_valid:
            form.save()
        return redirect("/")
    return render(request, 'tasks/edit.html', context)


def delete(request, pk):
    taskToDelete = Task.objects.get(id=pk)

    if request.method == 'POST':
        taskToDelete.delete()
        return redirect("/")
    context = {'taskToDelete': taskToDelete}
    return render(request, 'tasks/delete.html', context)
