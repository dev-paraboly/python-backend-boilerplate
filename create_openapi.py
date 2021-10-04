from fastapi.openapi.utils import get_openapi
from {{cookiecutter.app_name}}_service.main import app

import json


with open('openapi.json', 'w') as f:
    json.dump(get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    ), f)