from rest_framework import serializers
from django.contrib.auth.models import User



class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', ]

    def validate_email(self, value):

        user = User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("Cette adresse e-mail existe déjà.")
        return value


