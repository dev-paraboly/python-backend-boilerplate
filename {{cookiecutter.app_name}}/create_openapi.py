from fastapi.openapi.utils import get_openapi
from {{cookiecutter.app_name.replace("-", "_")}}_service.main import sub_app

import json


with open('openapi.json', 'w') as f:
    json.dump(get_openapi(
        title=sub_app.title,
        version=sub_app.version,
        openapi_version=sub_app.openapi_version,
        description=sub_app.description,
        routes=sub_app.routes,
    ), f)
