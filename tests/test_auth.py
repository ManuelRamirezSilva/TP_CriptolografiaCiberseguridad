from src.auth.login import LoginManager
from src.auth.password_manager import hash_password, verify_password
from src.auth.session_manager import SessionManager

def test_login_success():
    login_manager = LoginManager()
    username = "test_user"
    password = "secure_password"
    hashed_password = hash_password(password)
    
    # Mock user creation
    login_manager.create_user(username, hashed_password)
    
    assert login_manager.login(username, password) == True

def test_login_failure():
    login_manager = LoginManager()
    username = "test_user"
    password = "secure_password"
    
    assert login_manager.login(username, password) == False

def test_logout():
    login_manager = LoginManager()
    username = "test_user"
    password = "secure_password"
    hashed_password = hash_password(password)
    
    # Mock user creation
    login_manager.create_user(username, hashed_password)
    login_manager.login(username, password)
    
    assert login_manager.logout(username) == True

def test_password_hashing():
    password = "my_password"
    hashed = hash_password(password)
    
    assert verify_password(password, hashed) == True
    assert verify_password("wrong_password", hashed) == False

def test_session_management():
    session_manager = SessionManager()
    username = "test_user"
    
    token = session_manager.create_session(username)
    assert session_manager.validate_session(token) == True
    assert session_manager.validate_session("invalid_token") == False