# Lab 8 Part 5
from flask import Flask
app = Flask(__name__)

# Hello World!
@app.route('/')
def hello_world():
    return 'Hello, World!'
