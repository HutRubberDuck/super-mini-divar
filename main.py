from os import environ
from models import Database, Province, City
from fastapi import FastAPI

# Connecting to database
db = Database(environ['SUPER_MINI_DIVAR_DB_URL'])
db.create_database()

dbsession = db.session_local # You can use this object to create queries


app = FastAPI()

@app.get("/province/")
def get_all_provinces():
    items = dbsession.query(Province).all()
    return items


@app.get("/province/{province_id}/")
def get_province_by_id(province_id: int):
    province = dbsession.query(Province).filter(Province.id == province_id).first()
    return province