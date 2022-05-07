# test_webhello.py
#
import re

import pytest

from webhello import app as hello_app


@pytest.fixture()
def app():
    app = hello_app
    # app.config.update({"TESTING": True, "DATABASE": "beer.db"})
    app.config.update({"TESTING": True})

    # other setup can go here

    yield app


# clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


def test_status(client):
    response = client.get("/status")

    assert b"Gin App with Python Flask!" in response.data
    assert b"Sqlite version 3" in response.data


def test_randocat(client):
    response = client.get("/").data.decode("utf-8")

    assert re.compile(r"cat: [A-z]").search(response)
