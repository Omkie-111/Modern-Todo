from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
