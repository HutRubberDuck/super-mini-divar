from os import environ
from models import Database

# Connecting to database
db = Database(environ['SUPER_MINI_DIVAR_DB_URL'])
db.create_database()

dbsession = db.session_local # You can use this object to create queries
