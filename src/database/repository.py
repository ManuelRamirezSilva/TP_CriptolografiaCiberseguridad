# filepath: /TP_login/TP_login/src/database/repository.py

class MockDatabase:
    def __init__(self):
        self.users = {}
        self.sessions = {}

    def add_user(self, user_id, user_data):
        self.users[user_id] = user_data

    def get_user(self, user_id):
        return self.users.get(user_id)

    def add_session(self, session_id, session_data):
        self.sessions[session_id] = session_data

    def get_session(self, session_id):
        return self.sessions.get(session_id)

# Mock implementation of database interaction functions

def create_user(user_id, user_data):
    db = MockDatabase()
    db.add_user(user_id, user_data)
    return f"User {user_id} created."

def retrieve_user(user_id):
    db = MockDatabase()
    user = db.get_user(user_id)
    return user if user else "User not found."

def create_session(session_id, session_data):
    db = MockDatabase()
    db.add_session(session_id, session_data)
    return f"Session {session_id} created."

def retrieve_session(session_id):
    db = MockDatabase()
    session = db.get_session(session_id)
    return session if session else "Session not found."