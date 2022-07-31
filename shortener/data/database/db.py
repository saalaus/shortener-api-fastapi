from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_STRING = "sqlite:///database.db"


base = declarative_base()


engine = create_engine(DB_STRING, connect_args={
                       "check_same_thread": False})
session = sessionmaker(bind=engine)

base.metadata.create_all(engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
