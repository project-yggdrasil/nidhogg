from typing import List, Optional

from sqlmodel import Field, SQLModel
from nidhogg import engine

# TODO mobs_ids into a list, but sqlite doesnt have an array type bc that would make too much sense
class DuelData(SQLModel, table=True):
    duel_id: int = Field(primary_key=True)
    mob_ids: int
    oleaf_version: Optional[str]
    client_version: Optional[str]


SQLModel.metadata.create_all(engine)
