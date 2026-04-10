from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

SQL_ALCHEMY_DATABASE_UEL = "postgresql://postgres:1122@localhost:5432/booklist"

engine = create_engine(SQL_ALCHEMY_DATABASE_UEL)

Session_local = sessionmaker(autocommit = False,autoflush=False,bind = engine)