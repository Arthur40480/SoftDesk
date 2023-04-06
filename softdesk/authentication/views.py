from rest_framework import generics
from django.contrib.auth import authenticate, login
from .serializers import UserSignupSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User


class UserCreate(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSignupSerializer


class UserList(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSignupSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



