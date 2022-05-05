
from os import stat
from uuid import uuid4
import datetime

from flask import (
    Blueprint, g, jsonify, request, session, abort, make_response
)

from RAMMN import db
# from RAMMN import cache
from RAMMN.AuthFactory import AuthenticatorFactory

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('')
def get_auth_link():

    reddit_auth = AuthenticatorFactory().get_authenticator("REDDIT")

    return reddit_auth.make_authorization_url()

@bp.route('/reddit_callback')
def reddit_callback():

    reddit_auth = AuthenticatorFactory().get_authenticator("REDDIT")

    error = request.args.get('error', '')
    if error:
        return "Error: " + error

    state = request.args.get('state', '')

    # if not cache.get(state):
    #     # Uh-oh, this request wasn't started by us!
    #     abort(403)

    code = request.args.get('code')

    access_token = reddit_auth.get_token(code)

    user = reddit_auth.get_user(access_token)

    session = db.get_session(user["id"])

    # this implements unsafe upsert
    if not session:
        session = str(uuid4())
        db.add_user(user["id"], user["name"])
        if(not db.add_session(user["id"], session)):
            # not sure this is the best return code
            abort(403)


    # return access token and set cookie for session store with expiration time less than 1 hour

    resp = make_response(jsonify(), 200)

    expire_time = datetime.datetime.now()
    expire_time = datetime.timedelta(hour=1)

    resp.set_cookie('session', session, expires=expire_time)

    # cache.set(session, user.id)

    resp.set_data(access_token)

    return resp
