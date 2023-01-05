from django.shortcuts import get_object_or_404

from .models import Todo
from .serializers import TodoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# function-based view

@api_view(["GET", "POST"])
def todo_list_create(request):

    if(request.method == "GET"):
        todos = Todo.objects.filter(is_done = False)
        serializer = TodoSerializer(todos, many = True)
        return Response(serializer.data)

    elif(request.method == "POST"):
        serializer = TodoSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE", "PUT"])
def todo_detail(request, id):

    todo = get_object_or_404(Todo, id = id)

    if(request.method == "GET"):
        serialize = TodoSerializer(todo)
        return Response(serialize.data)

    elif(request.method == "PUT"):
        serializer = TodoSerializer(todo, data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            message = {
                "message": f"{todo.task} is updated"
            }
            return Response(message)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif(request.method == "DELETE"):

        todo.delete()
        return Response({"message": f"{todo.task} is deleted"})



# class-based views (concrete views)

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class Todos(ListCreateAPIView):

    queryset = Todo.objects.filter(is_done = False)
    serializer_class = TodoSerializer

class TodoDetail(RetrieveUpdateDestroyAPIView):

    queryset = Todo.objects.filter(is_done = False)
    serializer_class = TodoSerializer
    lookup_field = "id"


# class-based views (ViewSets)

from rest_framework.viewsets import ModelViewSet


class TodoMVS(ModelViewSet):

    queryset = Todo.objects.filter(is_done = False)
    serializer_class = TodoSerializer
    lookup_field = "id"