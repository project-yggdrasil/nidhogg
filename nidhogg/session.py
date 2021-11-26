from dataclasses import dataclass
from itertools import count


@dataclass
class Session:
    session_id: int
    oleaf_version: str
    client_version: str


class SessionManager:
    def __init__(self):
        self.sessions = {}
        self._id_gen = count(0, 1)

    async def new_session(self, oleaf_version: str, client_version: str) -> Session:
        """
        Creates a new session
        """
        session_id = next(self._id_gen)
        session = Session(session_id, oleaf_version, client_version)

        self.sessions[session_id] = session
        return session

    async def get_session(self, session_id: int) -> Session:
        """
        Get a session by id
        """
        try:
            return self.sessions[session_id]
        except KeyError:
            raise AttributeError(f"No session with id {session_id}")
