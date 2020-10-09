import pytest

from flask import Flask, request, render_template, session

from getflix.repository.memory_repo import MemoryRepo
from getflix.domainmodel.actor import Actor
from getflix.domainmodel.director import Director
from getflix.domainmodel.genre import Genre
from getflix.domainmodel.movie import Movie
from getflix.domainmodel.review import Review
from getflix.domainmodel.user import User
from getflix.domainmodel.watchlist import Watchlist

from getflix import create_app


def get_auth_status(responseData):
    html = str(responseData)
    statusTag = '<span id="AuthStatus" style="display:none;">'
    statusStart = html.index(statusTag) + len(statusTag)
    statusEnd = statusStart
    while html[statusEnd] != "<":
        statusEnd += 1
    return html[statusStart:statusEnd]

def get_auth_message(responseData):
    html = str(responseData)
    messageTag = '<p id="AuthMessage">'
    messageStart = html.index(messageTag) + len(messageTag)
    messageEnd = messageStart
    while html[messageEnd] != "<":
        messageEnd += 1
    return html[messageStart:messageEnd]


@pytest.fixture
def client():
    test_app = create_app()
    test_app.testing = True
    return test_app.test_client()


def test_register(client):
    response = client.get("/register?RegUsername=bob&RegPassword1=Mypassword1&RegPassword2=Mypassword1")
    authStatus = get_auth_status(response.data)
    authMessage = get_auth_message(response.data)
    assert authStatus == "logged in"
    assert authMessage == ""

def test_login(client):
    pass

def test_logout(client):
    pass