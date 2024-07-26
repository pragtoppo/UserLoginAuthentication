from django.db import models
import random
import hmac
import hashlib
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class OTP(models.Model):
    email = models.EmailField()
    otp_hash = models.CharField(max_length=64)
    expires_at = models.DateTimeField()

    @staticmethod
    def generate_otp():
        return ''.join(random.choices('0123456789', k=6))

    @staticmethod
    def hash_otp(otp, secret_key='my_secret_key'):
        # Use HMAC and SHA-256 for hashing
        return hmac.new(secret_key.encode(), otp.encode(), hashlib.sha256).hexdigest()

    def is_expired(self):
        return timezone.now() > self.expires_at
