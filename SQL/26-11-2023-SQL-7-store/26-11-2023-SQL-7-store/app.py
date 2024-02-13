from flask import Flask, session, request, render_template, redirect
import db

app = Flask(__name__)

app.secret_key="xvklsdoiisdfjhsdfklksdf;lsdfkjhsdkjjsdfkjh"

@app.route('/')
def home():
    if "cart" not in session:
        session["cart"]=[]
    products=db.get_products()
    return render_template("products.html", products=products, companies=[t[0] for t in db.query("SELECT name FROM companies")])

@app.route('/delete')
def delete():
    uid=request.args["id"]
    db.query(f"DELETE FROM users WHERE id={uid}")
    return render_template("users.html", users=db.get_users())

@app.route('/cart/buy')
def add_to_cart():
    session["cart"].append(request.args["id"])
    return redirect("/")

@app.route('/update')
def update_get():
    return render_template("update.html", user=User(username=request.args["username"], uid=request.args["id"]))

@app.route('/update', methods=['POST'])
def update_post():
    db.query(f"UPDATE users SET username='{request.form['username']}' WHERE id='{request.form['id']}'")
    return redirect("/")

@app.route('/companies/<name>')
def get_company(name):
    return render_template("company.html", company=db.get_company(name=name))

