"""
Simple in-memory user repository for testing purposes
"""

class UserRepository:
    def __init__(self):
        self.users = {}
        self._init_default_users()
    
    def _init_default_users(self):
        """Initialize with default test users"""
        # Password for both is "password123"
        default_users = {
            "admin": {
                'id': 1,
                'username': 'admin',
                'email': 'admin@example.com',
                'hashed_password': '$argon2id$v=19$m=65536,t=3,p=4$79ptAkiXIQx9QdNYd1BlZw$6u+RHygrr+oCX3eFk+tgHbVAp84PR8qYF1fFPpZT4gE'
            },
            "user": {
                'id': 2,
                'username': 'user',
                'email': 'user@example.com',
                'hashed_password': '$argon2id$v=19$m=65536,t=3,p=4$79ptAkiXIQx9QdNYd1BlZw$6u+RHygrr+oCX3eFk+tgHbVAp84PR8qYF1fFPpZT4gE'
            }
        }
        self.users.update(default_users)
    
    def add_user(self, username, email, hashed_password):
        """Add a new user to the repository"""
        if username in self.users:
            return None
        
        # Check if email already exists
        if any(u['email'] == email for u in self.users.values()):
            return None
        
        user_id = max([u['id'] for u in self.users.values()], default=0) + 1
        user = {
            'id': user_id,
            'username': username,
            'email': email,
            'hashed_password': hashed_password
        }
        self.users[username] = user
        return user
    
    def get_user_by_username(self, username):
        """Get a user by username"""
        return self.users.get(username)
    
    def get_user_by_id(self, user_id):
        """Get a user by ID"""
        for user in self.users.values():
            if user['id'] == user_id:
                return user
        return None
    
    def get_user_by_email(self, email):
        """Get a user by email"""
        for user in self.users.values():
            if user['email'] == email:
                return user
        return None
    
    def update_password(self, username, new_hashed_password):
        """Update user password"""
        if username in self.users:
            self.users[username]['hashed_password'] = new_hashed_password
            return True
        return False
    
    def user_exists(self, username):
        """Check if a user exists"""
        return username in self.users
    
    def email_exists(self, email):
        """Check if an email is already registered"""
        return any(u['email'] == email for u in self.users.values())
