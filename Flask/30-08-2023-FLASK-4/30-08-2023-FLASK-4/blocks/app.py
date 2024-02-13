from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/products')
def producs():
    return render_template("products.html")

@app.route('/shop')
def shop():
    return render_template("shop.html")
