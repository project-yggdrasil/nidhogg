class Session:
    def __init__(self):
        pass

    async def commit_to_db(self):
        pass


class SessionManager:
    def __init__(self):
        self.sessions = set()

    async def new_session(self) -> Session:
        """
        Creates a new session
        """
        pass

    async def get_session(self, session_id: int) -> Session:
        """
        Get a session by id
        """
        pass
