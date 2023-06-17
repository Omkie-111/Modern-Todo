from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoItem
from rest_framework_simplejwt.tokens import RefreshToken

class TodoItemSerializer(serializers.ModelSerializer):
    """
    Serializer for all todo functionalities
    """

    class Meta:
        model = TodoItem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating User model
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class TokenObtainPairSerializer(serializers.Serializer):
    """
    Serializer for obtaining token pair for authentication
    """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            else:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')
