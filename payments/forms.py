import datetime
from django import forms
from .models import Payment, Task


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
    deadline = forms.ChoiceField(
        choices=[(datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, x),
                  ('%s-%s-%s' % (str(x), datetime.datetime.now().month, datetime.datetime.now().year)))
                 for x in range(1, 32)], required=True)

    class Meta:
        model = Task
        fields = ['name', 'deadline']
