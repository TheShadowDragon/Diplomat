import json
from time import time
import cryptocode
from flask import (
    Flask,
    abort,
    redirect,
    render_template,
    request,
    send_file,
    send_from_directory,
    url_for,
)
from werkzeug.datastructures import ImmutableMultiDict
from flask import session
from random import randrange

post = open("templates/index.html", "r").read()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Main")
def Main():
    return (
            open("templates/index.html", "r")
            .read()
            .replace("^Title^", "Main")
            .replace("^webpage^", open("templates/main.html", "r").read())
        )

@app.route("/About")
def about():
    return (
            open("templates/index.html", "r")
            .read()
            .replace("^Title^", "About")
            .replace("^webpage^", open("templates/about.html", "r").read())
        )

if __name__ == "__main__":
    app.run(debug=True)