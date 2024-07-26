# User Login API with Email and OTP Authentication
Project Description
This project implements a backend API for user authentication using email and One-Time Password (OTP). Users can register with their email, receive an OTP, and verify it to gain access. The API ensures secure and efficient authentication processes.

Objectives
User Authentication: Implement a smooth authentication flow using email and OTP.
Security: Provide a secure authentication process to protect against threats like brute-force attacks and unauthorized access.
Key Features
Email Registration:

Endpoint to register users with an email address.
Validates email format and ensures uniqueness.
OTP Generation and Sending:

Endpoint to request an OTP.
Secure OTP generation.
Mock email service to print the OTP instead of sending it.
OTP Verification:

Endpoint to verify OTP.
Authenticates users if the OTP is valid and within the time limit.
Session Management:

Generate and manage user sessions upon successful OTP verification.
Issue secure session tokens for authenticated users.
Security Measures:

Rate limiting on OTP requests to prevent abuse.
Secure algorithms for OTP generation and hashing.
Encrypted communication between client and server.
Technical Requirements
Backend Framework: Django (or any other backend framework if preferred).
Database: SQLite.
Email Service: Integrate a mock email service to print OTPs instead of sending them.
Token Management: Use JWT (JSON Web Tokens) or a similar method for session tokens.
Env Setup: Optional Docker setup for environment configuration.
API Endpoints
User Registration:

Endpoint: POST /api/register
Request Body:
json
Copy code
{
  "email": "user@example.com"
}
Response:
json
Copy code
{
  "message": "Registration successful. Please verify your email."
}
Request OTP:

Endpoint: POST /api/request-otp
Request Body:
json
Copy code
{
  "email": "user@example.com"
}
Response:
json
Copy code
{
  "message": "OTP sent to your email."
}
Verify OTP:

Endpoint: POST /api/verify-otp
Request Body:
json
Copy code
{
  "email": "user@example.com",
  "otp": "123456"
}
Response:
json
Copy code
{
  "message": "Login successful.",
  "token": "jwt_token"
}
Setup and Installation
Clone the Repository:

sh
Copy code
git clone https://github.com/your-username/UserLoginAuthentication.git
cd UserLoginAuthentication
Create and Activate a Virtual Environment:

sh
Copy code
python -m venv env
source env/bin/activate  # On Windows use: .\env\Scripts\activate
Install Dependencies:

sh
Copy code
pip install -r requirements.txt
Apply Migrations:

sh
Copy code
python manage.py migrate
Run the Development Server:

sh
Copy code
python manage.py runserver
Testing
To run tests, ensure you have the necessary testing framework installed, and then execute:

sh
Copy code
pytest
Notes
The mock email service prints the OTP to the console instead of sending emails.
Adjust the time.sleep() duration in tests based on rate limit settings.
