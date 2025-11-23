"""Unit tests for additional `User` model helpers.

TDD: tests first to exercise `__repr__` and `to_dict` methods.
"""
from datetime import datetime

from app.models import User


def test_user_repr_and_to_dict():
    user = User()
    user.id = 42
    user.username = "tester"
    user.email = "tester@example.com"
    user.password_hash = "hashed"
    # set created_at explicitly since server_default happens in DB
    user.created_at = datetime(2020, 1, 1)

    r = repr(user)
    assert "User" in r and "tester" in r

    d = user.to_dict()
    assert d["id"] == 42
    assert d["username"] == "tester"
    assert d["email"] == "tester@example.com"
    assert "password_hash" not in d
    assert d["created_at"] == user.created_at
