from rest_framework import generics
from .models import TodoItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import TodoItemSerializer,UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogoutAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class ListTodo(generics.ListAPIView):
    """API Class to read all the todo items"""

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class DetailTodo(generics.RetrieveAPIView):
    """API Class to read one specific todo item"""

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class CreateTodo(generics.CreateAPIView):
    """API Class to create the todo items"""

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class UpdateTodo(generics.RetrieveUpdateAPIView):
    """API Class to update todo items"""

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class DeleteTodo(generics.DestroyAPIView):
    """API Class to delete the todo items"""

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
