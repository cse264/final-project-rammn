from flask import (
    Blueprint, request, session, abort
)

from RAMMN import db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
def get_user():
    if uid != session["store"][request.cookies.get("session")]:
        return abort(403)
    return db.get_user(session["store"][request.cookies.get("session")])

@bp.route('/activity')
def get_recent_users():
    return db.get_most_recent_users()

@bp.route('/volume')
def get_users_by_most_searches():
    return db.get_users_by_total_search_history()

@bp.route('/privileges')
def get_user_privileges():
    return db.get_user_privileges(session["store"][request.cookies.get("session")])

@bp.route('/history', methods = ['POST', 'GET'])
def user_history():
    uid = session["store"][request.cookies.get("session")]
    if request.method == 'GET':
        return db.get_user_search_history(uid)
    else:
        return db.add_user_search_history(uid, request.form["search_term"])

@bp.route('/history')
def users_history():
    return db.get_most_recent_search_history()

@bp.before_request
def before_request():
    session_id = request.cookies.get('session')
    if (session_id not in session["store"]):
        abort(403)