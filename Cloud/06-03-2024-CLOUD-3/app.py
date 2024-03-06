from flask import Flask
from flask_cors import CORS
import json
import sqlite3
import datetime

app=Flask(__name__)
CORS(app)

sqlite3.connect("visits.db").cursor().execute("CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY, date TEXT)")

@app.route("/")
def register_visit():
    with sqlite3.connect("visits.db") as conn: 
        cur=conn.cursor()
        cur.execute(f"INSERT INTO visits (date) VALUES ('{str(datetime.date.today())}')")
        return json.dumps({"visit registered":"ok"})

@app.route("/test")
def test():
    return json.dumps(sqlite3.connect("visits.db").cursor().execute("select * from visits").fetchall())
