from rest_framework import generics
from django.contrib.auth import authenticate, login
from .serializers import UserSignupSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Users


class UserCreate(generics.CreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UserSignupSerializer

    def validate_email(self, request):
        email = request.data.get('email')
        user = Users.objects.all(email=email)
        if user:
            return Response({'message': 'Cette adresse e-mail existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Cette adresse e-mail est unique.'}, status=status.HTTP_201_CREATED)


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
