from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session



URL = "postgresql://postgres:1050@localhost:5432/projectv"

engine = create_engine(url=URL)

SessionLocal= sessionmaker(bind=engine)

Base = declarative_base()



def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

     