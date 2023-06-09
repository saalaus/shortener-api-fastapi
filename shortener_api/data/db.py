from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

DB_STRING = "sqlite:///database.db"


base = declarative_base()


engine = create_engine(DB_STRING, connect_args={
                       "check_same_thread": False})
session = sessionmaker(bind=engine)

def get_db() -> Generator[Session, None, None]:
    """Get db dependecies."""
    db = session()
    try:
        yield db
    finally:
        db.close()
