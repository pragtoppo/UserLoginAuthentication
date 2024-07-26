from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
import pytest
import re
import time

def extract_otp_from_log(log_entry):
    """
    Extract OTP from the log entry.

    Args:
        log_entry (str): The log entry containing the OTP.

    Returns:
        str: The extracted OTP if found, otherwise None.
    """
    # Example regex to extract a 6-digit OTP
    otp_pattern = r"OTP (\d{6})"
    match = re.search(otp_pattern, log_entry)
    if match:
        return match.group(1)
    return None


@pytest.mark.django_db
def test_register():
    client = APIClient()
    response = client.post(reverse('register'), {'email': 'test@example.com'})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['message'] == 'Registration successful. Please verify your email.'

@pytest.mark.django_db
def test_otp_request():
    # First, register the user
    client = APIClient()
    client.post(reverse('register'), {'email': 'test@example.com'})

    # Request OTP
    response = client.post(reverse('request_otp'), {'email': 'test@example.com'})
    assert response.status_code == status.HTTP_200_OK
    assert response.data['message'] == 'OTP sent to your email.'