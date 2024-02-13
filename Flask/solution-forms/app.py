from flask import Flask, render_template, request, redirect
app = Flask(__name__)

users=[]

logged_in=False

products=[{"name":"nike", "price":"100"}, {"name":"adidas", "price":"200"}, {"name":"gali","price":"500"}]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/products')
def myproducts():
    return render_template("products.html", products=products)

@app.route('/shop')
def shop():
    if logged_in:
        return render_template("shop.html")
    else:
        return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    for user in users:
        if request.form["username"]==user["email"] and request.form["password"]==user["password"]:
            global logged_in
            logged_in=True
            return redirect("/shop")
    return redirect("/register")

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST":
        users.append(dict(request.form))
        return redirect("/")
