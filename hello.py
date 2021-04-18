from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # needs more cowbell
    return "Hello, World!"
