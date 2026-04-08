from sqlalchemy import Integer , column , String
from db import Base

class Book(Base):
    __tablename__ = "Books"

    id = column(Integer,primary_key = True,index = True)
    title = column(String , index = True)
    description = column(String , index = True)
    author = column(String , index = True)
    year = column(String , index = True)