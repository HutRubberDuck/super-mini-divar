from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from .core.database import Base, database
from .core.openapi import defined_openapi
from .core.settings import APP_NAME, APP_DESCRIPTION, APP_VERSION, JWT_SECRET_KEY
from .router import users, province

Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    licence_info=dict(name='Apache 2.0', url='https://www.apache.org/licenses/LICENSE-2.0.html'),
    docs_url='/docs',
    redoc_url='/docs/re',
)

app.include_router(province.router)
app.include_router(users.router)


@app.exception_handler(AuthJWTException)
def auth_jwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@AuthJWT.load_config
def get_config() -> List[tuple]:
    return [("authjwt_secret_key", JWT_SECRET_KEY)]


@app.get("/")
async def root():
    return {"message": "API Works Well! :)"}


app.openapi = defined_openapi
