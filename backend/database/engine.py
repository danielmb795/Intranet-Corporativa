from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

class Base(DeclarativeBase):
    pass


engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit =False
    )
