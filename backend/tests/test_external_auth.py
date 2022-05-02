from flask import g
import pytest
from RAMMN.external_auth import AuthenticatorFactory

def test_make_new_reddit_authenticator():
    option = "REDDIT"
    redditAuth = AuthenticatorFactory().get_authenticator(option)
    assert option in g
    assert redditAuth == g[option]