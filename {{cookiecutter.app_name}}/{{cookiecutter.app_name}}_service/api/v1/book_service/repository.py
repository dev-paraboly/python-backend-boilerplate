from sqlalchemy import select

from {{cookiecutter.app_name}}_service.middlewares import db_session_middleware
from {{cookiecutter.app_name}}_service.models.book import Book


class BookRepository:
    def get_book_query(self, book_id: str, session: db_session_middleware):
        query = select(Book).where(Book.book_id == book_id)
        result = session.execute(query).scalars().one()
        return result