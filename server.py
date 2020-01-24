
from uuid import uuid4
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("start.html")


@app.route("/get_session")
def get_new_session():
    session_id = uuid4()
    return ""
