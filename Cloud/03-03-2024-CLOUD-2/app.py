
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, session, request
import random
import sqlite3
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key=b"sadasdads"

def save(user="none", message="none"):
    with sqlite3.connect("chat.db") as conn:
        conn.cursor().execute("insert into chat values (?,?)", (user, message))

def load():
    with sqlite3.connect("chat.db") as conn:
        return conn.cursor().execute("select * from chat").fetchall()

@app.route('/')
def chat():
    if "username" not in session:
        session["username"]=f"user{random.randrange(1,100)}"
    #return f'{session["username"]} says {request.args["message"]}'
    save(user=session["username"], message=request.args["message"])
    return "".join([f"<div style='display:flex; gap:10px'><div>{i[0]}:</div><div>{i[1]}</div></div>" for i in load()])

@app.route('/api/chat')
def api_chat():
    if "username" not in session:
        session["username"]=f"user{random.randrange(1,100)}"
    #return f'{session["username"]} says {request.args["message"]}'
    save(user=session["username"], message=request.args["message"])
    return json.dumps([{"username":i[0], "message":i[1]} for i in load()])

@app.route('/api/notes')
def api_notes():
    return  json.dumps([{"note":"note1"}, {"note":"note2"}, {"note":"note3"}])



