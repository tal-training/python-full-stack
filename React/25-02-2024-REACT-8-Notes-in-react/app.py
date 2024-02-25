from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/notes')
def get_notes():
    return  ["note1", "note2", "note3"]

