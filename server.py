
from uuid import uuid4
from flask import Flask, escape, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def root():
    return redirect(url_for("start"))


@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "GET":
        return render_template("start.html")
    else:
        return "new session"


@app.route("/get_session")
def get_new_session():
    session_id = uuid4()
    return ""
