from sqlmodel import SQLModel, create_engine, Session
from app.helpers.models import Hero

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)
session = Session(engine)
