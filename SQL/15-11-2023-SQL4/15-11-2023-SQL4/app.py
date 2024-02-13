from flask import Flask, session, request, render_template, redirect
import db
from classes import User

app = Flask(__name__)

app.secret_key="xvklsdoiisdfjhsdfklksdf;lsdfkjhsdkjjsdfkjh"

@app.route('/')
def home():
    if "username" in session:
        return render_template("users.html", users=db.get_users())
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        if len(db.query(f"SELECT username, password FROM users WHERE username='{username}' AND password='{password}'"))>0:
            session["username"]=username
            return redirect("/")
        return "unauthorized"

@app.route('/delete')
def delete():
    uid=request.args["id"]
    db.query(f"DELETE FROM users WHERE id={uid}")
    return render_template("users.html", users=db.get_users())

@app.route('/add', methods=['POST'])
def add_user():
    db.add_user(User(username=request.form["username"], password=request.form["password"]))
    return render_template("users.html", users=db.get_users())
