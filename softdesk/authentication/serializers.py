from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        user = User.objects.create(password=password, **validated_data)
        return user

    def validate_email(self, value):

        """
        Méthode pour vérifier que l'adresse email n'existe pas déjà.
        """
        user = User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("Cette adresse e-mail existe déjà.")
        return value