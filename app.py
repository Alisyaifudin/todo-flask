from flask import Flask, jsonify, request
from db import db
from routes import task
from flask_cors import CORS
import os
# from dotenv import load_dotenv
# load_dotenv()

FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://127.0.0.1:5173')


app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": FRONTEND_URL}})

@app.route('/')
def welcome():
    return "Welcome to Todo Flask!"

get = task.GET(db)
@app.route(get.route(), methods=[get.method()])
def get_tasks():
    result = get.call()
    return jsonify(result)

add = task.ADD(db)
@app.route(add.route(), methods=[add.method()])
def add_task():
    body = request.get_json()
    input = add.get_input(body)
    result = add.call(input)
    return jsonify(result)

edit = task.EDIT(db)
@app.route(edit.route(), methods=[edit.method()])
def edit_task():
    body = request.get_json()
    input = edit.get_input(body)
    result = edit.call(input)
    return jsonify(result)
