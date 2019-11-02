from rest_framework import serializers

from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    """ Serializes registration requests and creates a new user. """

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
