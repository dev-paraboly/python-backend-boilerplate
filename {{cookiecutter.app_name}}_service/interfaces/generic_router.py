from fastapi import APIRouter

class GenericRouter:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):
        return self.router

    def bind_routes(self):
        raise NotImplementedError()