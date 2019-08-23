import datetime
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Task name', 'style': 'width: 400px'}), label=False)
    deadline = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ), required=True)
    category = forms.CharField(required=False)
    tag = forms.CharField(required=False)

    class Meta:
        model = Task
        fields = ['name', 'assigned', 'category', 'tag', 'description', 'deadline']
