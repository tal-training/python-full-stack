from flask import Flask, request
app = Flask(__name__)

# GET /echo?input=1
# {"result": 1}

@app.route('/echo')
def echo():
    return {"result":request.args['input']}



