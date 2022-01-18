from fastapi import FastAPI

from .core.database import Base, database
from .core.settings import APP_NAME, APP_DESCRIPTION, APP_VERSION
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


@app.get("/")
async def root():
    return {"message": "API Works Well! :)"}
