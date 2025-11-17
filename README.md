# Secure Login Project

This project is a secure login system designed for a Cryptography and Cybersecurity course. It implements various security measures and best practices to ensure user authentication and data protection.

## Project Structure

```
TP_login
├── src
│   ├── auth
│   ├── crypto
│   ├── security
│   ├── database
│   ├── web
│   ├── static
│   ├── config
│   └── utils
├── tests
├── docs
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Functional Requirements

1. **User Authentication**: The system must allow users to log in and log out securely.
2. **Password Management**: Passwords must be hashed and verified using Argon2id.
3. **Session Management**: User sessions must be managed securely with token generation and validation.
4. **Input Validation**: All user inputs must be validated to prevent injection attacks.
5. **Rate Limiting**: Implement rate limiting to prevent brute force attacks on login.

## Non-Functional Requirements

1. **Security**: The application must adhere to security best practices, including secure password storage and session management.
2. **Performance**: The application should handle multiple concurrent users efficiently.
3. **Maintainability**: The code should be modular and easy to maintain.
4. **Documentation**: The project must include comprehensive documentation for setup and usage.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd TP_login
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables by copying `.env.example` to `.env` and updating the values as needed.

5. Run the application:
   ```
   python main.py
   ```

## Usage

- Navigate to `http://localhost:5000` in your web browser to access the login interface.
- Users can log in with their credentials, and upon successful authentication, they will be redirected to the dashboard.

## Testing

To run the tests, use the following command:
```
pytest tests/
```

## Security Analysis

Refer to `docs/security_analysis.md` for a detailed analysis of the security measures implemented in this project. 

## Acknowledgments

This project is developed as part of the Cryptography and Cybersecurity course.