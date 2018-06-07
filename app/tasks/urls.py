from django.urls import path
from tasks.views import *

urlpatterns = [
    path("", show_tasks, name="tasks"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("task/<slug:slug>/", show_task, name="task")
]