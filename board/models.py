from django.conf import settings
from django.db import models


class Task(models.Model):
    STATUSES = [
        ("To Do", "todo"),
        ("Doing", "doing"),
        ("Done", "done"),
        ("Backlog", "backlog"),
    ]

    name = models.CharField(max_length=200)
    status = models.CharField(
        choices=STATUSES, blank=True, default="todo", max_length=64
    )
    done_ind = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    assigned = models.ForeignKey('accounts.UserProfile', on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=100, default=None)
    tag = models.CharField(max_length=50, default=None)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    deadline = models.DateField()

    def __str__(self):
        return self.name
