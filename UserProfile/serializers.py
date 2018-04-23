from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Token, Profile


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

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ('bio', 'hobbies', 'birth_date')
