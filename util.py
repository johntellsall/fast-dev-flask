import sqlite3

# from flask import current_app, g

# TODO: handle missing database -- sqlite3.OperationalError


def get_db():
    # if "db" not in g:
    con = sqlite3.connect(
        # current_app.config["DATABASE"],
        "cat.sqlite",
        detect_types=sqlite3.PARSE_DECLTYPES,
    )
    con.row_factory = sqlite3.Row

    return con


def query1(con, sql):
    result = con.execute(sql)
    return result.fetchall()[0][0]
