from django.shortcuts import render, redirect
from .models import Task


# Create your views here.
def listTask(request):
    tasks = Task.objects.all()
    return render(request, 'listTask.html', {'tasks': tasks})


def createTask(request):
    print(request.POST)
    task = Task(title=request.POST['title'], description=request.POST['description']) #Insert into
    task.save()     # Guarda los datos
    return redirect('/task/')


def deleteTask(request, idTask):
    task = Task.objects.get(id=idTask)
    task.delete()

    return redirect('/task/')
