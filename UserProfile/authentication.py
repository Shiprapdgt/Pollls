from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from .models import Token

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print('*' * 100, request.META)
        key = request.META.get('HTTP_AUTHORIZATION',)

        if not key:
            return None, None

        try:
            token = Token.objects.get(key=key)
            user = token.user
        except Token.DoesNotExist:
            return None, None
        return user, token

