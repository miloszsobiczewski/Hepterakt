import datetime
from django import forms
from .models import Task
from django.utils.safestring import mark_safe


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'style': 'width: 400px'}),)
    deadline = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ), required=True)
    category = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 400px'}),)
    tag = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'style': 'width: 400px'}),)

    class Meta:
        model = Task
        fields = ['name', 'assigned', 'category', 'tag', 'description', 'deadline']
