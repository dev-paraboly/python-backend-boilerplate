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

    def get_book_list_query(self, session: db_session_middleware):
        query = session.query(Book).all()
        return query


    def create_book_query(self, book: Book, session: db_session_middleware):
        book_db = Book(
            book_id = book.book_id,
            author = book.author,
            book_name = book.book_name,
            description = book.description,
            book_type = book.book_type,
        )
        query = session.query(Book).filter(Book.book_id == book.book_id).first()
        if query:
            raise HTTPException(status_code=400, detail=f"Book item with id {book.book_id} already exists")
        else:
            session.add(book_db)
            session.commit()
            session.close()
            return book

    def update_book_query(self, book_db, book, session):
        book_db.author = book.author
        book_db.book_name = book.book_name
        book_db.description = book.description
        book_db.book_type = book.book_type
        session.commit()
        session.close()
        return book_db

    def delete_book_query(self, book_id: str, session: db_session_middleware):
        book_db = self.get_book_query(book_id, session)
        if book_db:
            session.delete(book_db)
            session.commit()
            session.close()
            return book_db
        else:
            raise HTTPException(status_code=404, detail=f"book item with id {book_id} not found")
