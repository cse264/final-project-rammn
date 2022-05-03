from flask import (
    Blueprint, request, session, abort
)

from RAMMN import db
from RAMMN import cache

bp = Blueprint('interests', __name__, url_prefix='/interests')

@bp.route('/', methods = ['POST', 'GET'])
def get_interests():
    if request.method == 'GET':
        return db.get_all_interests()
    else:
        return db.add_interest(request.form["interest"], request.form["description"])

@bp.route('/user/')
def add_user_interest():
    return add_user_interest(session["store"][request.cookies.get("session")], request.form["interests"])

@bp.before_request
def before_request():
    session_id = request.cookies.get('session')
    if not cache.get(session_id):
        abort(403)