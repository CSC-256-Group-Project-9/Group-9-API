from sqlalchemy import Column, Integer, String
from config import Base

class Student(Base):
    __tablename__ = 'students'

    id=Column(Integer, primary_key=True)
    fname=Column(String)
    lname=Column(String)
    #fav=Column(String)