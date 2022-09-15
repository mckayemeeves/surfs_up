# import dependencies
from flask import Flask
# creates a flask instance "singular version of something"
app = Flask(__name__)
# create the flask route
@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/')
def name():
    return 'my name is mckaye'