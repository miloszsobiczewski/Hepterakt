import os
from datetime import timedelta, datetime
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
        navigate = request.POST.get('Navigate', False)
        if navigate:
            pass
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
        now = datetime.now()
        form = TaskForm()
        tasks.filter(date__range=(datetime(now.year, now.month, 1), datetime(now.year, now.month, 31)))
    return render(request, "payments/tasks.html", {'tasks': tasks,
                                                   'form': form})


def payments_view(request, curr_year=None, curr_month=None):
    if curr_month is None:
        curr_month = datetime.now().month
    if curr_year is None:
        curr_year = datetime.now().year
    payments = Payment.objects.all().order_by('-id').filter(date__month=curr_month, date__year=curr_year)
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
    # distinct months for page filtering
    payments_dates = Payment.objects.values_list('date', flat=True)
    payments_months = list(set([x.month for x in payments_dates]))
    payments_years = list(set([x.year for x in payments_dates]))
    return render(request, "payments/payments.html", {'payments': payments,
                                                      'payments_months': payments_months,
                                                      'payments_years': payments_years,
                                                      'curr_month': curr_month,
                                                      'curr_year': curr_year,
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
