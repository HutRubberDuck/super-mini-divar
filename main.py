from models import Database

DATABASE_URL = ""

# Connecting to database
db = Database(DATABASE_URL)
db.create_database()

dbsession = db.session_local # You can use this object to create queries



