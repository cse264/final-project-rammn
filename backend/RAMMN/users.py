from flask import (
    Blueprint, request, session, abort
)

from RAMMN import db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
def get_user():
    user_id = db.get_user_from_session(request.cookies.get("session"))
    user = db.get_user(user_id)
    if not user:
        return abort(404)
    return user

@bp.route('/activity')
def get_recent_users():
    return db.get_most_recent_users()

@bp.route('/volume')
def get_users_by_most_searches():
    return db.get_users_by_total_search_history()

@bp.route('/privileges')
def get_user_privileges():
    return db.get_user_privileges(db.get_user_from_session(request.cookies.get("session")))

@bp.route('/history', methods = ['POST', 'GET'])
def user_history():
    uid = db.get_user_from_session(request.cookies.get("session"))
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
    if not db.get_user_from_session(session_id):
        abort(403)