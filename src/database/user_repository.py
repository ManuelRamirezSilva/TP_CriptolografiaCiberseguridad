"""
Simple in-memory user repository for testing purposes
"""

class UserRepository:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, email, hashed_password):
        """Add a new user to the repository"""
        if username in self.users:
            return None
        
        user_id = len(self.users) + 1
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
