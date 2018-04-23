from django.contrib.auth import authenticate
from uuid import uuid4
from .models import Token, Profile
from rest_framework.views import APIView
# from urllib import request
from django.contrib.auth.models import User
from .serializers import UserSerializer, TokenSerializer, ResponseSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .authentication import TokenAuthentication
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer


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
            print(response_serializer.data)
            return Response(response_serializer.data)
        else:
            return "Authentication failed"


class ProfileViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        print(request.META.get('HTTP_AUTHORIZATION'))
        bio = request.POST['bio']
        hobbies = request.POST['hobbies']
        birth_date = request.POST['birth_date']
        user = Token.objects.get(key=request.META.get('HTTP_AUTHORIZATION')).user
        profile_obj = Profile(user=user, bio=bio, hobbies=hobbies, birth_date=birth_date)
        profile_obj.save()
        response_serializer = ProfileSerializer(profile_obj)
        return Response(response_serializer)

    def update(self, request, *args, **kwargs):
        user = Token.objects.get(key=request.META.get('HTTP_AUTHORIZATION')).user
        profile_obj = Profile.objects.get(user=user)
        if request.POST['bio'] is not None:
            bio = request.POST['bio']
            profile_obj.update(bio=bio)

        if request.POST['hobbies'] is not None:
            hobbies = request.POST['hobbies']
            profile_obj.update(hobbies=hobbies)

        if request.POST['birth_date'] is not None:
            birth_date = request.POST['birth_date']
            profile_obj.update(birth_date=birth_date)

    def destroy(self, request, *args, **kwargs):
        user = Token.objects.get(key=request.META.get('HTTP_AUTHORIZATION')).user
        profile = Profile.objects.get(user=user).delete()