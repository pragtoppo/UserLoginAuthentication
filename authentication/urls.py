# authentication/urls.py
from django.urls import path
from .views import UserRegistrationView, OTPRequestView, OTPVerificationView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('request-otp/', OTPRequestView.as_view(), name='request_otp'),
    path('verify-otp/', OTPVerificationView.as_view(), name='verify_otp'),
]
