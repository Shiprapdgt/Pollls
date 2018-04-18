from django.contrib.auth import authenticate
from uuid import uuid4
from .models import Token
from rest_framework.views import APIView
# from urllib import request
from django.contrib.auth.models import User
from .serializers import UserSerializer, TokenSerializer, ResponseSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .authentication import TokenAuthentication


class Login(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print('*' * 100, user, 2)
        if user is not None:
            rand_token = uuid4()
            t_obj = Token(user=user, key=rand_token)
            t_obj.save()
            responseData = {
                'user': UserSerializer(user).data,
                'token': TokenSerializer(t_obj).data
            }

            response_serializer = ResponseSerializer(responseData)
            return Response(response_serializer.data)
        else:
            return "Authentication failed"


class Logout(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        Token.objects.get(key=token).delete()
        return Response("logged out")
