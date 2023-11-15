"""
Database Schema configs

@author Anthony Epps
"""

from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class StudentSchema(BaseModel):
    id: Optional[int]=None
    fname: Optional[str]=None
    lname: Optional[str]=None
    #fav: Optional[str]=None

    class Config:
        orm_mode = True

class RequestStudent(BaseModel):
    parameter: StudentSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]