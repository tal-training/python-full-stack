from flask_cors import CORS
from flask import Flask, request
import random

app = Flask(__name__)
CORS(app)

number=random.randrange(1,10)

@app.route('/api/test/number')
def test_number():
    return {"number":number}

@app.route('/api/guess', methods=['GET', 'POST'])
def guess():
    user_guess=int(request.args.get('number', request.json['number']))
    if user_guess==number:
        return {"result":"win"}
    if user_guess<number:
        return {"result":"low"}
    else:
        return {"result":"high"}
        
@app.route('/api/guess/range', methods=['POST'])
def set_range():
    global number
    number=random.randrange(int(request.json["low"]),int(request.json["high"]))
    return {"number":number}

