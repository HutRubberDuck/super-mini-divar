import uvicorn

from src.core.settings import APP_HOST, APP_PORT, DEBUG

if __name__ == "__main__":
    uvicorn.run("src.main:app", host=APP_HOST, port=APP_PORT, reload=DEBUG)
