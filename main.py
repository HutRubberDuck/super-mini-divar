import uvicorn

from src.core.settings import APP_HOST, APP_PORT, DEBUG
from src.main import app

if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT, reload=DEBUG)
