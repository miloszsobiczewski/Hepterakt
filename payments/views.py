import os
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Payment, Task, Month
from .forms import PaymentForm, TaskForm, MonthForm


def go_admin(request):
    return HttpResponseRedirect('/admin/')


def docs_view(request):
    return render(request, "payments/documents.html")


def hours_view(request):
    hours = Month.objects.all().order_by('-id')
    if request.method == 'POST':
        form = MonthForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MonthForm()
    return render(request, "payments/hours.html", {'hours': hours,
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
            dates = tasks.values_list('id', 'deadline')
            updated_dates = [(x[0], x[1] + relativedelta(months=1)) for x in dates]
            [tasks.filter(pk=x[0]).update(deadline=x[1]) for x in updated_dates]
        else:
            form = TaskForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
        form = TaskForm()
    else:
        form = TaskForm()
    warning_date = date.today() + timedelta(days=7)
    return render(request, "payments/tasks.html", {'tasks': tasks,
                                                   'form': form,
                                                   'warning_date': warning_date})


def payments_view(request, curr_year=None, curr_month=None):
    if curr_month is None:
        curr_month = datetime.now().month
    if curr_year is None:
        curr_year = datetime.now().year
    payments = Payment.objects.all().order_by('-id').filter(date__month=curr_month, date__year=curr_year)
    if request.method == 'POST':
        edit_payments = Payment.objects.all().order_by('-id')
        paid = request.POST.get('Done', False)
        if paid:
            edit_payments.filter(pk=paid).update(paid=True)
            form = PaymentForm()
        else:
            form = PaymentForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), {'form': form,
                                                                            'payments': payments})
    else:
        form = PaymentForm()
    # distinct months for page filtering
    payments_dates = Payment.objects.values_list('date', flat=True)
    payments_months = list(set([x.month for x in payments_dates]))
    payments_months.sort(reverse=True)
    payments_years = list(set([x.year for x in payments_dates]))
    payments_years.sort(reverse=True)
    month_total = sum([value for value in payments.values_list('value', flat=True)])
    return render(request, "payments/payments.html", {'payments': payments,
                                                      'payments_months': payments_months,
                                                      'payments_years': payments_years,
                                                      'curr_month': curr_month,
                                                      'curr_year': curr_year,
                                                      'month_total': month_total,
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
