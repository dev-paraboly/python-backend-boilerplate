from sqlalchemy import select
from fastapi import HTTPException

from {{cookiecutter.app_name.replace("-", "_")}}_service.middlewares import db_session_middleware
from {{cookiecutter.app_name.replace("-", "_")}}_service.models.book import Book


class BookRepository:
    def get_book_query(self, book_id: str, session: db_session_middleware):
        
        query = session.query(Book).filter(Book.book_id == book_id).first()
        if query :
            return query
        else:
            raise HTTPException(status_code=404, detail=f"book item with id {book_id} not found")