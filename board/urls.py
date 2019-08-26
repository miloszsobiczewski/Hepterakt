from django.conf.urls import url

from . import views

app_name = "board"

urlpatterns = [
    url(r"^$", views.board, name="board"),
    url(r"^task/(?P<task_id>[-\w]+)/$", views.edit_task, name="edit-task"),
    url(r"^closed/", views.closed, name="closed"),
]
