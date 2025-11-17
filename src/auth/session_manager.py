from datetime import datetime, timedelta
import jwt

class SessionManager:
    def __init__(self, secret_key, algorithm='HS256', expiration_minutes=30):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expiration_minutes = expiration_minutes

    def create_session_token(self, user_id):
        expiration = datetime.utcnow() + timedelta(minutes=self.expiration_minutes)
        token = jwt.encode({'user_id': user_id, 'exp': expiration}, self.secret_key, algorithm=self.algorithm)
        return token

    def validate_session_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def refresh_session_token(self, token):
        user_id = self.validate_session_token(token)
        if user_id:
            return self.create_session_token(user_id)
        return None