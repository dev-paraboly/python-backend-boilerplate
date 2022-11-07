import json

from typing import Optional

from enum import Enum

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

from pydantic import BaseModel

Base = declarative_base()
from .helper import OrmHelper

class FixedBookTypeExample(str, Enum):
    HORROR = 'horror'
    FANTASTIC = 'fantastic'

class Book(Base):
    __tablename__ = 'book'
    __table_args__ = {'schema': 'public'}
    
    book_id: str = Column(String, primary_key=True)
    author: str = Column(String, primary_key=True)
    book_name: str = Column(String, primary_key=False)
    description: str = Column(String, primary_key=False)
    book_type: str = Column(String, primary_key=False)

    def __repr__(self) -> str:
        return json.dumps(self.dict())

    def __str__(self) -> str:
        return json.dumps(self.dict())

    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class BookPydantic(BaseModel):
    author : Optional[str]
    book_name: Optional[str]
    description: Optional[str]
    book_type: Optional[FixedBookTypeExample]