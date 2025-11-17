class LoginManager:
    def __init__(self, password_manager, session_manager, user_repository=None):
        self.password_manager = password_manager
        self.session_manager = session_manager
        self.user_repository = user_repository

    def login(self, username, password):
        user = self.get_user(username)
        if user and self.password_manager.verify_password(password, user['hashed_password']):
            token = self.session_manager.create_session_token(user['id'])
            return token
        return None

    def logout(self, token):
        # Session token validation would be needed here
        # For now, we just acknowledge the logout
        return True

    def get_user(self, username):
        # Use repository if available, otherwise fallback to mock
        if self.user_repository:
            return self.user_repository.get_user_by_username(username)
        
        # Mock implementation: Replace with actual database call
        # Password for both users is "password123"
        # Hashed with Argon2
        mock_users = {
            "admin": {
                "id": 1, 
                "username": "admin",
                "email": "admin@example.com",
                "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$79ptAkiXIQx9QdNYd1BlZw$6u+RHygrr+oCX3eFk+tgHbVAp84PR8qYF1fFPpZT4gE"
            },
            "user": {
                "id": 2, 
                "username": "user",
                "email": "user@example.com",
                "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$79ptAkiXIQx9QdNYd1BlZw$6u+RHygrr+oCX3eFk+tgHbVAp84PR8qYF1fFPpZT4gE"
            },
        }
        return mock_users.get(username)