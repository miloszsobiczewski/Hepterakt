import os
from datetime import datetime, date, timedelta
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Task
from .forms import TaskForm


def board(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    # import pdb; pdb.set_trace()
    return render(request, "board/board.html", {'tasks': tasks,
                                                'form': form})


def edit_task(request, task_id):
    task = Task.objects.filter(pk=task_id)
    # import pdb; pdb.set_trace()

    return render(request, "board/edit_task.html", {'tasks': task})


