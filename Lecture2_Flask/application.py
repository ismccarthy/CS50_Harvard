import datetime
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    new_year = True
    # return render_template('Web001.html', new_year=new_year)
    return render_template('Web001.html', new_year=new_year)


# @app.route("/")
# def index():
#     return "Hello World!"

# @app.route("/")
# def index():
#     headline = "This is Page One!"
#     return render_template('Web001.html', headline=headline)
#
#
# @app.route("/today")
# def today():
#     now = datetime.datetime.now()
#     headline = f'Today it is.. {now}'
#
#     sunday = 1 == 1
#
#     # return render_template('Web001.html', headline=headline)
#     return render_template('Web001.html', sunday=sunday)


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
