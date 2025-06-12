# user/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

# Validation and serialization for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)

    class Meta:
        model= User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user= User(
            username= validated_data['username'],
            email= validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user