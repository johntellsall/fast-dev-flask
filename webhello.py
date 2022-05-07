# webhello.py

import random

from flask import Flask

import util

app = Flask(__name__)


@app.route("/status")
def status():
    con = util.get_db()
    version = util.query1(con, "select sqlite_version()")
    return f"Gin App with Python Flask! -- Sqlite version {version}"


@app.route("/")
def home():
    con = util.get_db()
    result = con.execute("select name from cat")
    names = [row["name"] for row in result]
    name = random.choice(names)
    return f"cat: {name}"
