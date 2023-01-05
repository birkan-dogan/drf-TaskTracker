from django.urls import path

from todo.views import (todo_list_create, todo_detail)

urlpatterns = [
    path("todo-create/", todo_list_create),
    path("todo-detail/<int:id>", todo_detail),
]
