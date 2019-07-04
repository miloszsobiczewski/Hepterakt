import os
from datetime import timedelta
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import F

from .models import Payment, Task
from .forms import PaymentForm, TaskForm


def go_admin(request):
    return HttpResponseRedirect('/admin/')


def docs_view(request):
    payments = Payment.objects.all().order_by('-id')
    form = []
    return render(request, "payments/documents.html", {'payments': payments,
                                                       'form': form})


def tasks_view(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        done = request.POST.get('Done', False)
        reset = request.POST.get('Reset', False)
        update = request.POST.get('UpDate', False)
        if done:
            tasks.filter(pk=done).update(done=True)
        if reset:
            tasks.update(done=False)
        if update:
            tasks.update(deadline=F('deadline') + timedelta(365 / 12))
        else:
            form = TaskForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
        form = TaskForm()
    else:
        form = TaskForm()
    return render(request, "payments/tasks.html", {'tasks': tasks,
                                                   'form': form})


def payments_view(request):
    payments = Payment.objects.all().order_by('-id')
    if request.method == 'POST':
        paid = request.POST.get('Done', False)
        if paid:
            payments.filter(pk=paid).update(paid=True)
            form = PaymentForm()
        else:
            form = PaymentForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
    else:
        form = PaymentForm()
    return render(request, "payments/payments.html", {'payments': payments,
                                                      'form': form})


def download(request):
    file_location = request.POST.get('FilePath', False)
    file_path = os.path.join(settings.MEDIA_ROOT, file_location)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
