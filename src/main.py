from fastapi import FastAPI

from .core.database import Base, database
from .router import users, province

Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title='Super Mini Divar',
    description='A simple Backend for Ads And Requirements System Like Divar',
    version='0.1.0',
    licence_info=dict(name='Apache 2.0', url='https://www.apache.org/licenses/LICENSE-2.0.html'),
    docs_url='/docs',
    redoc_url='/docs/re',
)

app.include_router(province.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "API Works Well! :)"}
