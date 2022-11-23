import {{cookiecutter.app_name.replace("-", "_")}}_service.settings

import uvicorn
import os
from fastapi import FastAPI, Depends

from {{cookiecutter.app_name.replace("-", "_")}}_service.api.v1.book_service.router import BookRouter
from .auth import get_auth

auth_dependencies = []
# For development purposes, can be improved
if os.getenv("ENV") != 'dev':
    auth_dependencies.append(Depends(get_auth))

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
    dependencies=auth_dependencies
)

sub_app.include_router(BookRouter().get_router(), prefix="/book_service")

app.mount("/v1/{{cookiecutter.app_name.replace("-", "_")}}", sub_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
