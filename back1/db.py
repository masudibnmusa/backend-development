from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_ALCHEMY_DATABASE_URL = "postgresql://postgres:1122@localhost:5432/bookstore"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind=engine)
Base = declarative_base()