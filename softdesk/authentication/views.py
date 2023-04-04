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


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Vous êtes connecté'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': "Nom d'utilisateur ou mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)
