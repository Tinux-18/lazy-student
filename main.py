from flask import Flask
from flask_cors import CORS

from query_mongo import get_progress

# Building Flask

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_lists():
    print("get me")
    # minutes = get_progress("Samuel Cochran", "62b707d4e700f67ac1e2eff7")._CommandCursor__data[0]

@app.route('/', methods=['POST'])
def get_progress():
    variable_name = request.args.get('student')
    print(variable_name)
    # minutes = get_progress("Samuel Cochran", "62b707d4e700f67ac1e2eff7")._CommandCursor__data[0]
