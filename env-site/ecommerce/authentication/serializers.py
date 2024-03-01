from rest_framework import serializers

from authentication.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','email','password')