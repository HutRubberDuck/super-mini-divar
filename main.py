from os import environ

from fastapi import FastAPI

from models import Database, Province

# Connecting to database
db = Database(environ['SUPER_MINI_DIVAR_DB_URI'])
db.create_database()

dbsession = db.session_local  # You can use this object to create queries

app = FastAPI()


@app.get("/province/")
def get_all_provinces():
    return dbsession.query(Province).all()


@app.get("/province/{province_id}/")
def get_province_by_id(province_id: int):
    return dbsession.query(Province).filter(Province.id == province_id).first()
