from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', )

class ResponseSerializer(serializers.Serializer):
    class Meta:
        fields = ('user', 'token')

    user = UserSerializer()
    token = TokenSerializer()
