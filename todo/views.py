from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class ListTodo(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
