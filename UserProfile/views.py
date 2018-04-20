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
from rest_framework import status, viewsets
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
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
