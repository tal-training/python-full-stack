from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key="fuiweriuyewryu"

users=["admin", "tal"]

@app.route('/')
def hello():
    if session.get("username", "")=="admin":
        return 'admin secret is 19'
    if session.get("username", "")=="tal":
        return 'tal secret is 17'
    else:
        return "unauthorized"
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:
        if (request.form["username"] in users) and (request.form["password"]=="admin"):
            session["username"]=request.form["username"]
            return redirect("/")
        return "unauthorized"
