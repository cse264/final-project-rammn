from flask import (
    Blueprint, request, session, abort
)

from RAMMN import db
import json

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
    return json.dumps(db.get_most_recent_users())

@bp.route('/volume')
def get_users_by_most_searches():
    return json.dumps(db.get_users_by_total_search_history())

@bp.route('/privileges')
def get_user_privileges():
    return json.dumps(db.get_user_privileges(db.get_user_from_session(request.cookies.get("session"))))

@bp.route('/history', methods = ['POST', 'GET'])
def user_history():
    uid = db.get_user_from_session(request.cookies.get("session"))
    if request.method == 'GET':
        return db.get_user_search_history(uid)
    else:
        return db.add_user_search_history(uid, request.form["search_term"])

@bp.route('/search/history')
def users_search_history():
    return json.dumps(db.get_most_recent_search_history())

@bp.route('/searches')
def users_searches():
    return str(db.get_search_history_count()[0])

@bp.route('/count')
def users_count():
    return str(db.get_users_count()[0])

# @bp.before_request
# def before_request():
#     session_id = request.cookies.get('session')
#     if not db.get_user_from_session(session_id):
#         abort(403)