from django.conf.urls import url

from . import views

app_name = "board"

urlpatterns = [
    url(r"^$", views.board, name="board"),
]
