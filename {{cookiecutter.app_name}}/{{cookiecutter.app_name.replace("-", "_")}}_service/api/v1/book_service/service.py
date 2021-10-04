from {{cookiecutter.app_name.replace("-", "_")}}_service.middlewares import db_session_middleware

from .repository import BookRepository

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def get_book(self, book_id: str, session: db_session_middleware):
        book = self.repository.get_book_query(book_id, session)
        return book
