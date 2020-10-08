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

@pytest.fixture
def client():
    test_app = create_app()
    test_app.testing = True
    return test_app.test_client()


def test_register(client, repo):
    response = client.get("/register?RegUsername=bob&RegPassword1=Mypassword1&RegPassword2=Mypassword1")
    assert response.status_code == 200
    # assert response.get("authStatus") == "logged in"
    # assert response.get("authMessage") == ""