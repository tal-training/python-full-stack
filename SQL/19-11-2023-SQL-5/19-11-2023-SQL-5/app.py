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
        user_tuples=db.query(f"SELECT id, username, password FROM users WHERE username='{username}' AND password='{password}'")
        if len(user_tuples)>0:
            session["username"]=username
            session["id"]=user_tuples[0][0]
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

@app.route('/update')
def update_get():
    return render_template("update.html", user=User(username=request.args["username"], uid=request.args["id"]))

@app.route('/update', methods=['POST'])
def update_post():
    db.query(f"UPDATE users SET username='{request.form['username']}' WHERE id='{request.form['id']}'")
    return redirect("/")

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method=='POST':
        db.query(f"UPDATE users SET password='{request.form['password']}' WHERE id='{session['id']}'")
        return redirect("/")
    else:
        return render_template("reset.html", username=session["username"])

@app.route('/reset_user', methods=['GET', 'POST'])
def reset_user():
    if request.method=='POST':
        db.query(f"UPDATE users SET password='{request.form['password']}' WHERE id='{request.form['id']}'")
        return redirect("/")
    else:
        return render_template("reset_user.html", username=request.args["username"], uid=request.args["id"])
