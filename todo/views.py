from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class ListTodo(generics.ListAPIView):
    """API Class to read all the todo items"""

    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class DetailTodo(generics.RetrieveAPIView):
    """API Class to read one specific todo item"""

    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class CreateTodo(generics.CreateAPIView):
    """API Class to create the todo items"""

    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class UpdateTodo(generics.RetrieveUpdateAPIView):
    """API Class to update todo items"""

    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class DeleteTodo(generics.DestroyAPIView):
    """API Class to delete the todo items"""

    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
