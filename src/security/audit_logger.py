class AuditLogger:
    def __init__(self, log_file='audit.log'):
        self.log_file = log_file

    def log_event(self, event):
        with open(self.log_file, 'a') as f:
            f.write(f"{event}\n")

    def log_login_attempt(self, username, success):
        event = f"Login attempt for user '{username}': {'Success' if success else 'Failure'}"
        self.log_event(event)

    def log_logout(self, username):
        event = f"User '{username}' logged out."
        self.log_event(event)

    def log_password_change(self, username):
        event = f"User '{username}' changed their password."
        self.log_event(event)