from fastapi import Depends, FastAPI
from sqlmodel import Session as DBSession
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from nidhogg import DuelData, engine


app = FastAPI()


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


@app.post("/auth/")
async def post_auth(version: str, client_version: str, authorize: AuthJWT = Depends()):
    # generate random session_id here
    access_token = authorize.create_access_token(subject=123)
    return {"access_token": access_token}


@app.post("/data/duel/")
async def post_duel(duel: DuelData, authorize: AuthJWT = Depends()):
    session_id = authorize.get_jwt_subject()

    with DBSession(engine) as db_session:
        db_session.add(duel)
        db_session.commit()
