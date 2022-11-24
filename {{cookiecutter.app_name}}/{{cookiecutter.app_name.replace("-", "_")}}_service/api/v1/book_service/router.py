from fastapi.params import Depends, Body

from {{cookiecutter.app_name.replace("-", "_")}}_service.middlewares import db_session_middleware
from {{cookiecutter.app_name.replace("-", "_")}}_service.interfaces.generic_router import GenericRouter
from {{cookiecutter.app_name.replace("-", "_")}}_service.models.book import BookPydantic
from .service import BookService

class BookRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = BookService()
        self.bind_routes()

    def bind_routes(self):
        self.get_router().get("/book/{book_id}", status_code=status.HTTP_200_OK)(self.get_book)
        self.get_router().post("/book", status_code=status.HTTP_201_CREATED)(self.create_book)
        self.get_router().put("/book/{book_id}", status_code=status.HTTP_200_OK)(self.update_book)
        self.get_router().delete("/book/{book_id}", status_code=status.HTTP_200_OK)(self.delete_book)
        self.get_router().get("/book", status_code=status.HTTP_200_OK)(self.get_book_list)

    def create_book(
        self,
        book: BookPydantic = Body(),
        session: db_session_middleware = Depends()
    ):
        return self.service.create_book(book, session)

    def update_book(
        self,
        book_id: str,
        book: BookPydantic = Body(),
        session: db_session_middleware = Depends(),
    ):
        return self.service.update_book(book_id, book, session)

    def delete_book(
        self,
        book_id: str,
        session: db_session_middleware = Depends(),
    ):
        return self.service.delete_book(book_id, session)

    def get_book_list(
        self,
        session: db_session_middleware = Depends(),
    ):
        return self.service.get_book_list(session)

    def get_book(
        self,
        book_id: str,
        session: db_session_middleware = Depends(),
    ):
        return self.service.get_book(book_id, session)
