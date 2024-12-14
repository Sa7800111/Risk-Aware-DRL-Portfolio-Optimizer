class SessionManager:
    def __init__(self):
        self.sessions = {}

    def start_session(self, user_id: str):
        self.sessions[user_id] = {"start": time.time(), "actions": 0}

    def log_action(self, user_id: str):
        if user_id in self.sessions:
            self.sessions[user_id]["actions"] += 1