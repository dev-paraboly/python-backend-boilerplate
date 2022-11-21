import os
import uvicorn

if __name__ == "__main__":
    # again for development purposes
    uvicorn.run("camera_api_service.main:app", host="0.0.0.0", port=8000, reload=True)
