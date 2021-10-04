import {{cookiecutter.app_name}}_service.settings

import uvicorn
from fastapi import FastAPI

from {{cookiecutter.app_name}}_service.api.v1.book_service.router import BookRouter

VERSION = "1.0.0"

app = FastAPI(
    title="Backend Service",
    version=VERSION,
    description="Backend service developed using fastapi",
)

sub_app = FastAPI(
    title="Backend Service",
    version=VERSION,
    description="Backend service developed using fastapi",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

sub_app.include_router(BookRouter().get_router(), prefix="/book_service")

app.mount("/v1/{{cookiecutter.app_name}}", sub_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
