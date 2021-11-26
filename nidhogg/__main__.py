from fastapi import Depends, FastAPI
from sqlmodel import Session as DBSession
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from nidhogg import DuelData, engine, SessionManager


app = FastAPI()
session_manager = SessionManager()


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


@app.post("/auth/")
async def post_auth(oleaf_version: str, client_version: str, authorize: AuthJWT = Depends()):
    session = await session_manager.new_session(oleaf_version, client_version)
    access_token = authorize.create_access_token(subject=session.session_id)
    return {"access_token": access_token}


@app.post("/data/duel/")
async def post_duel(duel: DuelData, authorize: AuthJWT = Depends()):
    session_id = authorize.get_jwt_subject()
    session = await session_manager.get_session(session_id)

    duel.oleaf_version = session.oleaf_version
    duel.client_version = session.client_version

    with DBSession(engine) as db_session:
        db_session.add(duel)
        db_session.commit()
