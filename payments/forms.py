import datetime
from django import forms
from .models import Payment, Task, Month


class PaymentForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width: 400px'}), label=False)
    value = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Value'}), label=False)
    description = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Description', 'style': 'width: 800px'}),
                                  label=False)
    invoice = forms.FileField(label=False, required=False)

    class Meta:
        model = Payment
        fields = ['name', 'paid', 'value', 'category', 'invoice', 'description']


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Task name', 'style': 'width: 400px'}), label=False)
    deadline = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ), required=True)

    class Meta:
        model = Task
        fields = ['name', 'deadline']


class MonthForm(forms.ModelForm):
    vacation_hours = forms.IntegerField(required=False)
    overtime_hours = forms.IntegerField(required=False)
    date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),)

    class Meta:
        model = Month
        fields = ['date', 'work_hours', 'vacation_hours', 'overtime_hours']
