from fastapi.params import Depends

from {{cookiecutter.app_name}}_service.middlewares import db_session_middleware
from {{cookiecutter.app_name}}_service.interfaces.generic_router import GenericRouter

from .service import BookService

class BookRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = BookService()
        self.bind_routes()    

    def bind_routes(self):
        self.get_router().get("/")(self.get_book)

    def get_book(
        self,
        book_id: str,
        session: db_session_middleware = Depends(),
    ):
        book = self.service.get_book(book_id, session)
        return {"book": book}
