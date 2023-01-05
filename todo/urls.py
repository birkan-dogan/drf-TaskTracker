from django.urls import path

from todo.views import (todo_list_create, todo_detail, Todos, TodoDetail)

urlpatterns = [
    # path("todo-create/", todo_list_create),
    # path("todo-detail/<int:id>", todo_detail),
    path("todo-create/", Todos.as_view()),
    path("todo-detail/<int:id>", TodoDetail.as_view()),
    # these two endpoints are doing the same job in just 2 lines of codes that function-based views do.
]
