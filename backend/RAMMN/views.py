from uuid import uuid4
import datetime
import time

from flask import (
    Blueprint, redirect, render_template, abort, request, session, make_response
)

from jinja2 import TemplateNotFound

from RAMMN import db
from RAMMN.AuthFactory import AuthenticatorFactory

sample_page = Blueprint('sample_page', 'sample_page', template_folder='templates')


@sample_page.route('/')
def get_sample():
    status = 200
    error = request.args.get('error', '')
    state = request.args.get('state', '')
    code  = request.args.get('code', '')
    resp = make_response(render_template('index.html'))
    try:
        if error or (state and code):
        # check if uri params are set for reddit auth
            # check cookies from session
            # call db to check session
            if not error:
                reddit_auth = AuthenticatorFactory().get_authenticator("REDDIT")
                access_token = reddit_auth.get_token(code)
                user = reddit_auth.get_user(access_token)
                session = db.get_session(user["id"])
                if not session:
                    session = str(uuid4())
                    db.add_user(user["id"], user["name"])
                    if(not db.add_session(user["id"], session)):
                        # not sure this is the best return code
                        abort(403)
                else:
                    session = session[0]
                
                expire_time = time.time() + 3600

                resp = make_response(redirect('/#/Home'))

                resp.set_cookie('session', session, expire_time)
                resp.set_cookie('access_token', access_token, expire_time)
                print(session)
                print(access_token)

                return resp, status

            else:
                state = 403
        elif state or code:
            state = 403

        return resp, status
    except TemplateNotFound:
        abort(404)