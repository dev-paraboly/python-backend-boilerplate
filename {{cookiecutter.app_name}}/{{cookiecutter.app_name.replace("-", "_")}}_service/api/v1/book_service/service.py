from {{cookiecutter.app_name.replace("-", "_")}}_service.middlewares import db_session_middleware
from {{cookiecutter.app_name.replace("-", "_")}}_service.models.book import BookPydantic
from .repository import BookRepository
from fastapi import HTTPException, status

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def get_book(self, book_id: str, session: db_session_middleware):
        book = self.repository.get_book_query(book_id, session)
        return book

    def get_book_list(self, session: db_session_middleware):
        book_list = self.repository.get_book_list_query(session)
        return book_list

    def create_book(self, book: BookPydantic, session: db_session_middleware):
        created_book = self.repository.create_book_query(book, session)
        return created_book

    def update_book(self, book_id: str, book: BookPydantic, session: db_session_middleware):
        book_db = self.repository.get_book_query(book_id, session)
        if book_db:
            self.repository.update_book_query(book_db, book, session)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    def delete_book(self, book_id: str, session: db_session_middleware):
        self.repository.delete_book_query(book_id, session)
