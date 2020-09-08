from rest_framework import serializers

from .models import User, Login, Verification


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'phone_number', 'is_verified', 'password')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('email', 'password')


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('id', 'email', 'otp', 'user_id')
