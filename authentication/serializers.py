from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import OTP

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email']

    def validate(self, data):
        if get_user_model().objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already registered.")
        return data

class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        if not get_user_model().objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email not registered.")
        return data

class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    def validate(self, data):
        try:
            otp_hash = OTP.hash_otp(data['otp'])
            otp_record = OTP.objects.get(email=data['email'], otp_hash=otp_hash)
            if otp_record.is_expired():
                raise serializers.ValidationError("OTP has expired.")
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP.")
        return data
