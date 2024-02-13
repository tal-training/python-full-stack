from flask import Flask, render_template, request
app = Flask(__name__)
import datetime
name=""

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/solutions')
def solutions():
    return render_template("solutions.html")

@app.route('/add/name/')
def add():
    name = request.args.get("username","")
    return render_template("solutions.html", name=name)

import pickle
def save(name):
    with open("name.pickle", 'wb') as f:
        pickle.dump(name, f)

def load():
    with open("name.pickle", 'rb') as f:
        return pickle.load(f)

@app.route('/add/name/save')
def store():
    save(request.args.get("username",""))
    return render_template("solutions.html", stored_name=load())

#, "date":str(datetime.datetime.now().strftime("%X"))}
names=[]
@app.route('/add/names')
def add_names():
    names.append(request.args["username"])
    return render_template("solutions.html", names=names)

info=[]
@app.route('/add/info')
def add_info():
    info.append({
        "name":request.args["username"], 
        "date":str(datetime.datetime.now().strftime("%X"))
    })
    return render_template("solutions.html", info=info)

@app.route('/add/info/home')
def add_info_home():
    info.append({
        "name":request.args["username"], 
        "date":str(datetime.datetime.now().strftime("%X"))
    })
    return render_template("home.html", info=info)


@app.route('/names')
def just_names():
    return render_template("names.html", info=info)

@app.route('/dates')
def dates():
    return render_template("dates.html", info=info)