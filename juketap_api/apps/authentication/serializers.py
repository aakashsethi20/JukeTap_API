from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    """ Serializer for registration requests and creates a new user. """

    password = serializers.CharField(
        min_length=8,
        max_length=128,
        write_only=True
    )

    token = serializers.CharField(
        max_length=255,
        read_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    """ Serializer for login requests. """

    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """
        Validates the credentials passed in the Login request.
        Raises ValidationError if credentials are wrong or if no user was found.
        Raises ValidationError if email or password is not provided.
        Raises ValidationError if account is no longer active.
        Returns user account identification attributes upon successful login.
        """

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with these credentials was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
