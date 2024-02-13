from flask import Flask, render_template, request, redirect, url_for
import functions
import files
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", contacts=files.load_contacts())

@app.route('/add')
def add():
    name=request.args["name"]
    phone=request.args["phone"]
    functions.add(name, phone)
    # return "contact added"
    return redirect(url_for('home'))

@app.route('/view')
def view():
    return str(functions.view())

@app.route('/delete')
def delete():
    name=request.args["name"]
    functions.delete(name)
    return redirect(url_for('home'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        name=request.form["name"]
        phone=request.form["phone"]
        functions.update(name=name, phone=phone)
        return redirect(url_for('home'))
    else:
        return render_template("update.html", name=request.args["name"], phone=request.args["phone"])