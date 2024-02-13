from flask import Flask, session, request, render_template, redirect, url_for
import db
from classes import Cart

app = Flask(__name__)

app.secret_key="xvklsdoiisdfjhsdfklksdflsdfkjhsdkjjsdfkjh"

@app.route('/')
def home():
    if "cart" not in session:
        session["cart"]=[]
    products=db.get_products()
    cart=[db.get_products(pid=i)[0] for i in session["cart"]]
    total=sum([p.price for p in cart])
    cart.append(total)
    return render_template("products.html", products=products, companies=[t[0] for t in db.query("SELECT name FROM companies")], cart=cart)

@app.route('/cart/buy')
def add_to_cart():
    l=session["cart"]
    l.append(request.args["id"])
    session["cart"]=l
    return redirect("/")

@app.route('/cart/clear')
def clear_cart():
    session["cart"]=[]
    return home()

@app.route('/companies/<name>')
def get_company(name):
    return render_template("company.html", company=db.get_company(name=name))

