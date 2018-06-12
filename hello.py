from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cox")
def hello_cox():
    return "Hello Cox!"

@app.route("/coxtest")
def hello_cox_test():
    return "Hello Cox_test!"
#Test
