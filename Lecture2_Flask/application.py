from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/nietzsche")
def nietzsche():
    return "Friedrich Wilhelm Nietzsche (1844-1900)"


@app.route("/ian")
def ian():
    return "<h1>Hello Ian</h1>"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello {name}!"
