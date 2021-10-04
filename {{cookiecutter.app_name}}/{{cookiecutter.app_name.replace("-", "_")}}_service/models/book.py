import json

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
from .helper import OrmHelper

class Book(Base):
    __tablename__ = 'book'
    __table_args__ = {'schema': 'public'}
    
    book_id: str = Column(String, primary_key=True)
    author: str = Column(String, primary_key=True)
    book_name: str = Column(String, primary_key=False)
    description: str = Column(String, primary_key=False)

    def __repr__(self) -> str:
        return json.dumps(self.dict())

    def __str__(self) -> str:
        return json.dumps(self.dict())

    def dict(self) -> dict:
        return OrmHelper.toDict(self)
