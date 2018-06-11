from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cox")
def hello_cox():
    return "Hello Cox!"