from flask import Flask, request
from functions import to100, smaller100
app = Flask(__name__)

@app.route('/to100')
def to100route():
    return {"result":to100()}

@app.route('/smaller100')
def smaller100route():
    return {"result":smaller100(request.args["num"])}