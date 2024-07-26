from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from .models import OTP
from datetime import timedelta
from .serializers import UserRegistrationSerializer, OTPRequestSerializer, OTPVerificationSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful. Please verify your email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPRequestView(views.APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = OTP.generate_otp()
            otp_hash = OTP.hash_otp(otp)
            otp_record = OTP.objects.create(
                email=email,
                otp_hash=otp_hash,
                expires_at=timezone.now() + timedelta(minutes=10)
            )
            # Mock sending email
            print(f"Sending OTP {otp} to {email}")
            return Response({"message": "OTP sent to your email."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPVerificationView(views.APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            otp_hash = OTP.hash_otp(otp)
            try:
                otp_record = OTP.objects.get(email=email, otp_hash=otp_hash)
                if not otp_record.is_expired():
                    user = get_user_model().objects.get(email=email)
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        "message": "Login successful.",
                        "token": str(refresh.access_token)
                    })
                return Response({"message": "OTP has expired."}, status=status.HTTP_400_BAD_REQUEST)
            except OTP.DoesNotExist:
                return Response({"message": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
