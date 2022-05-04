import psycopg2
from config import URI

db = psycopg2.connect(URI, sslmode="require")
cursor = db.cursor()

def psql_create():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id TEXT, username TEXT, fullname TEXT);")
        db.commit()
    except:
        cursor.execute("rollback")
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id TEXT, username TEXT, fullname TEXT);")
        db.commit()

def psql_film_create():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS film (photo TEXT, discription TEXT);")
        db.commit()
    except:
        cursor.execute("filmback")
        cursor.execute("CREATE TABLE IF NOT EXISTS film (photo TEXT, discription TEXT);")
        db.commit()