from flask_cors import CORS
from flask import Flask, request
import random

app = Flask(__name__)
CORS(app)

number=random.randrange(1,10)

@app.route('/api/guess')
def guess():
    user_guess=int(request.args['number'])
    if user_guess==number:
        return {"result":"win"}
    if user_guess<number:
        return {"result":"low"}
    else:
        return {"result":"high"}
        
    

