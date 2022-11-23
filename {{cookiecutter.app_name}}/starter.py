import os
import uvicorn

if __name__ == "__main__":
    # again for development purposes
    uvicorn.run("{{cookiecutter.app_name.replace("-", "_")}}_service.main:app", host="0.0.0.0", port=8000, reload=True)
