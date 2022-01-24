from fastapi import FastAPI

from .core.config import config
from .core.database import database
from .core.middleware import AppCORSMiddleware
from .router import users, province, primary, city, district, category, advertising, otp

app = FastAPI(**config)


@app.on_event("startup")
def on_startup():
    database.init_db()


app.add_middleware(AppCORSMiddleware)

app.include_router(primary.router)
app.include_router(province.router)
app.include_router(otp.router)
app.include_router(users.router)
app.include_router(city.router)
app.include_router(district.router)
app.include_router(category.router)
app.include_router(advertising.router)
