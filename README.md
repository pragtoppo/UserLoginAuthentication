# User Login API with Email and OTP Authentication

## Project Description
This project implements a backend API for user authentication using email and One-Time Password (OTP). Users can register with their email, receive an OTP, and verify it to gain access. The API ensures secure and efficient authentication processes.

## Objectives
1. **User Authentication**: Implement a smooth authentication flow using email and OTP.
2. **Security**: Provide a secure authentication process to protect against threats like brute-force attacks and unauthorized access.

## Key Features
### 1. Email Registration
- **Endpoint**: `POST /api/register`
- **Description**: Register users with an email address.
- **Validation**: Email format is validated, and uniqueness is ensured.

### 2. OTP Generation and Sending
- **Endpoint**: `POST /api/request-otp`
- **Description**: Request an OTP.
- **Process**: Generate a secure OTP and mock email service to print it.

### 3. OTP Verification
- **Endpoint**: `POST /api/verify-otp`
- **Description**: Verify the OTP.
- **Process**: Authenticate users if the OTP is valid and within the time limit.

### 4. Session Management
- **Description**: Generate and manage user sessions upon successful OTP verification.
- **Token**: Issue secure session tokens for authenticated users.

### 5. Security Measures
- **Rate Limiting**: Implemented on OTP requests to prevent abuse.
- **Algorithms**: Secure algorithms for OTP generation and hashing.
- **Communication**: Encrypted communication between client and server.

## Technical Requirements
1. **Backend Framework**: Django (or any other backend framework if preferred).
2. **Database**: SQLite.
3. **Email Service**: Integrate a mock email service to print OTPs instead of sending them.
4. **Token Management**: Use JWT (JSON Web Tokens) or a similar method for session tokens.
5. **Env Setup**: Optional Docker setup for environment configuration.

## API Endpoints
### 1. User Registration
- **Endpoint**: `POST /api/register`
- **Request Body**:
  ```json
  {
    "email": "user@example.com"
  }

