from django.urls import path
from .views import *

urlpatterns = [
    path('', ListTodo.as_view()),
    path('signup/', UserCreateAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),
    path('detail/<int:pk>', DetailTodo.as_view()),
    path('create/', CreateTodo.as_view()),
    path('update/<int:pk>', UpdateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view()),
]
