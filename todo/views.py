from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import TodoItem
from .serializers import (
    TodoItemSerializer,
    UserCreateSerializer,
    TokenObtainPairSerializer
)


class UserCreateAPIView(generics.CreateAPIView):
    """
    API Class to create todo list user
    """

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserLoginAPIView(generics.GenericAPIView):
    """
    API Class to login user
    """

    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if user is not None:
            login(request, user)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



class UserLogoutAPIView(APIView):
    """
    API Class to logout user
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logout(request)
        response_data = {
            'detail': 'Successfully logged out.'
        }
        return Response(response_data, status=status.HTTP_200_OK)


class ListTodo(generics.ListAPIView):
    """
    API Class to read all the todo items
    """

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class DetailTodo(generics.RetrieveAPIView):
    """
    API Class to read one specific todo item
    """

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class CreateTodo(generics.CreateAPIView):
    """
    API Class to create the todo items
    """

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class UpdateTodo(generics.RetrieveUpdateAPIView):
    """
    API Class to update todo items
    """

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class DeleteTodo(generics.DestroyAPIView):
    """
    API Class to delete the todo items
    """

    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
