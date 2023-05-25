from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_complated=False).order_by('-updated_at')
    complated_task = Task.objects.filter(is_complated=True)

    context = {
        "tasks": tasks,
        'complated_task': complated_task
    }
    return render(request, 'home.html', context)