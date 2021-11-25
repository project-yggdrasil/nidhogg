from sqlmodel import create_engine

engine = create_engine("sqlite:///database.db")
del create_engine

from .models import DuelData
