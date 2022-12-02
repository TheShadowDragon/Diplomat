'''
<a href=#^user^ style="size: 10px;">^user^</a>
'''
import json
from time import time
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
#pip install Flask-login
from flask_login import current_user, LoginManager, login_user, logout_user, login_required, UserMixin
from flask import session
import random
from flask import Flask, request, jsonify
from datetime import datetime
#pip install email_validator

global logged_in
global local_user
logged_in = False
local_user = "register"
def logreg_display():
    if logged_in is True:
        return local_user
    return "Register/Login"

def logreg_redirect():
    if logged_in is True:
        return url_for('user', user_link=local_user)
    return "register"

display = "Login/Register"
post = open("templates/index.html", "r").read()
app = Flask(__name__)

@app.route("/")
def index():
    return (
        open("templates/index.html", "r")
        .read()
        .replace("^logreg_redirect^", logreg_redirect())
        .replace("^logreg_display^", logreg_display())
        .replace("^webpage^", "")
        .replace("^Title^", "Home")
    )

@app.route("/Main")
def Main():
    return (
            open("templates/index.html", "r")
            .read()
            .replace("^Title^", "Main")
            .replace("^logreg_redirect^", logreg_redirect())
            .replace("^logreg_display^", logreg_display())
            .replace("^webpage^", open("templates/main.html", "r").read())
        )

@app.route("/About")
def about():
    return (
            open("templates/index.html", "r")
            .read()
            .replace("^Title^", "About")
            .replace("^logreg_redirect^", logreg_redirect())
            .replace("^logreg_display^", logreg_display())
            .replace("^webpage^", open("templates/about.html", "r").read())
        )

@app.route("/register", methods=["GET", "POST"])
def register():
    global logged_in
    global local_user
    sessname = session.get("name", "Login")
    form = """
    <div class=posts>
        <form action="/register">
            <label for="id1">Email: </label>
            <input type="text" id="id1" name="email">
            <br>
            <label for="id2">Username: </label>
            <input type="text" id="id2" name="name">
            <br>
            <label for="id3">Password:  </label>
            <input type="text" id="id3" name="password">
            <br>
            <label for="id4">Re-Enter Password:  </label>
            <input type="text" id="id4" name="password_verification">
            <br>
            <input type="submit" value="Submit">
        </form>
    </div>"""
    get_users = json.loads(open("json/users.json", "r").read())
    email = request.args.get("email")
    name = request.args.get("name")
    password = request.args.get("password")
    password_verification = request.args.get("password_verification")
    
    if name == None or password == None or email == None or password_verification == None:
        return (
                open("templates/index.html", "r")
                .read()
                .replace("^Title^", logreg_display())
                .replace("^logreg_redirect^", logreg_redirect())
                .replace("^logreg_display^", logreg_display())
                .replace("^webpage^", form)
            )


    for item in get_users:
        if name == item:
            return (
                open("templates/index.html", 'r')
                .read()
                .replace("^logreg_redirect^", logreg_redirect())
                .replace("^logreg_display^", logreg_display())
                .replace("^webpage^", "User already exists." + form)
            )
    
    add_user = open("json/users.json", 'w')
    get_users.update({name: {"password": password}})
    add_user.write(json.dumps(get_users, indent=2))
    logged_in = True
    local_user = name
    return (
        open("templates/index.html", 'r')
        .read()
        .replace("^logreg_redirect^", logreg_redirect())
        .replace("^logreg_display^", logreg_display())
        .replace("^webpage^", open("templates/user.html", 'r').read())
    )


@app.route("/profile/<user_link>")
def user(user_link):
    global local_user
    global logged_in
    return (
            open("templates/index.html", "r")
            .read()
            .replace("^Title^", local_user)
            .replace("^logreg_redirect^", logreg_redirect())
            .replace("^logreg_display^", logreg_display())
            .replace("^webpage^", open("templates/user.html", "r").read())
        )


if __name__ == "__main__":
    app.run(debug=True)