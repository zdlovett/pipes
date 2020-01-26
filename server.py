
from uuid import uuid4
from datetime import datetime as dt
from datetime import timedelta as td
from datetime import timezone as tz
from flask import Flask, escape, render_template, redirect, url_for, request

app = Flask(__name__)


pipes = {}


class Pipe:
    def __init__(self):
        self.created = dt.now(tz.utc)
        self.clients = []

    def add_client(self, client):
        if client not in self.clients:
            self.clients.append(client)


def uuid_exists(uuid: str):
    return uuid in pipes


def new_pipe() -> str:
    uuid = str(uuid4())
    pipes[uuid] = Pipe()
    return uuid


@app.route("/")
def root():
    return redirect(url_for("show_start"))


@app.route("/start", methods=["GET", "POST"])
def show_start():

    if request.method == "GET":
        return render_template("start.html")

    else:  # process the post
        pipe_uuid = request.values.get("pipe_id")

        if not uuid_exists(pipe_uuid):
            pipe_uuid = new_pipe()

        return redirect(url_for("show_pipe", pipe_uuid=pipe_uuid))


@app.route("/pipe/<pipe_uuid>")
def show_pipe(pipe_uuid: str):

    if uuid_exists(pipe_uuid):
        return render_template("pipe.html", pipe_uuid=pipe_uuid)

    return redirect(url_for("show_start"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
