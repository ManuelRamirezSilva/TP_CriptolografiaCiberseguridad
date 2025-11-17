class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}

    def is_allowed(self, user_id):
        current_time = time.time()
        if user_id not in self.requests:
            self.requests[user_id] = []

        # Remove outdated requests
        self.requests[user_id] = [timestamp for timestamp in self.requests[user_id] if timestamp > current_time - self.time_window]

        if len(self.requests[user_id]) < self.max_requests:
            self.requests[user_id].append(current_time)
            return True
        return False

    def reset(self, user_id):
        if user_id in self.requests:
            del self.requests[user_id]