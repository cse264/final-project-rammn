from flask import g
import pytest
from RAMMN.external_auth import AuthenticatorFactory

def test_make_new_reddit_authenticator():
    option = "REDDIT"
    AuthenticatorFactory(option)
    assert option in g