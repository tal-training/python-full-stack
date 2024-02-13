from flask import Flask, render_template, request
app=Flask(__name__)
import datetime
import random

class Contact:
    def __init__(self, name="", phone="", email="") -> None:
        self.name=name
        self.phone=phone
        self.email=email

class Task:
    def __init__(self, name="", description="", date="") -> None:
        self.name=name
        self.description=description
        self.date=date


contact_dict={"name":"tal", "phone":"053-222222", "email":"tal@al.com"}

contacts=[
    Contact(name="tal", phone="053-33333", email="tal@tal.com"),
    Contact(name="gal", phone="054-33333", email="gal@tal.com"),
    Contact(name="zal", phone="055-33333", email="zal@tal.com")
    ]

tasks=[
    Task(name="tal task", description="clean house", date="10/10/2023"),
    Task(name="gal task", description="walk dog", date="10/11/2023"),
    Task(name="home task", description="clean home", date="12/10/2023"),
    ]

@app.route('/')
def home():
    tal=Contact(name="tal", phone="052-33333", email="tal@tal.com")
    return render_template("index.html", contact=contact_dict, contacts=contacts, tasks=tasks, date=datetime.date.today()) 

# http://localhost:5000/code?coupon=123445


@app.route('/code/<coupon>')
def code(coupon):
    if coupon=="12345":
        return render_template("coupon.html", num=10)
    if coupon=="123456":
        return render_template("coupon.html", num=15)
    if coupon=="1234567":
        return render_template("coupon.html", num=20)
    return "bad coupon"

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", name=username)

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return str(int(num1)+int(num2))

@app.route('/add')
def add2():
    return str(int(request.args["num1"])+int(request.args["num2"]))

@app.route('/phone/<name>')
def phone(name):
    phones={"tal":"054-213323"}
    return phones.get(name, "phone does not exist")

rand_num=random.randint(1,10)

@app.route('/game/<num>')
def game(num):
    num=int(num)
    if num==rand_num:
        return render_template("game.html", message="YOU WON!!!")
    if num<rand_num:
        return render_template("game.html", message="too small")
    if num>rand_num:
        return render_template("game.html", message="too big")

