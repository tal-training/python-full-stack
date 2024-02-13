from flask import Flask, render_template, request
app=Flask(__name__)
import datetime

@app.route('/')
def hello():
    return render_template("targilim.html")

@app.route('/targil1')
def targil1():
    return render_template("targil1.html", name=request.args["username"], date=datetime.datetime.today())


@app.route('/targil2')
def hello_response():
    if request.args['username']=="tal":
        message=f"Hello, {request.args['username']}"
    else:
        message="Unauthorized"
    return render_template("targil2.html", message=message)

@app.route('/targil3')
def targil3():
    return render_template("targil3.html", firstname=request.args["firstname"], lastname=request.args["lastname"])

@app.route('/targil4')
def targil4():
    price=request.args["price"]
    result=int(price)*1.17
    return render_template("targil4.html", result=str(result))

@app.route('/targil5')
def targil5():
    result=str(int(request.args["num1"])+int(request.args["num2"]))
    return render_template("targil5.html", result=result)

