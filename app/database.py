import os

from fastapi import HTTPException
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://root:root@postgis/intelimetrica?port=5432"
)
# postgresql+psycopg2://user:password@host:port/dbname

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as error:
        raise HTTPException(status_code=500, detail="Internal Server Error") from error
    finally:
        db.close()
