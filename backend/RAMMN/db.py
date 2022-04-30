from unittest import result
import psycopg2
import sys
import click
from flask import current_app, g
from flask.cli import with_appcontext            

def get_db():
    if 'db' not in g:
        try:
            g.db = psycopg2.connect(current_app.config['DATABASE_URL'])
        except psycopg2.DatabaseError as e:
            print(e, file=sys.stderr)
            raise e

    return g.db

def example_method():
    """This function is an example on how to execute queries with cursor"""
    db = get_db()

    query = "SELECT * FROM tb1"

    with db.cursor() as cursor:
        cursor.execute(query)
        records = [row for row in cursor.fetchall()]
        cursor.close()
        return records

# prepared statements set, functions that execute them
# pgadmin
#   log into heroku
#    -> settings, config vars (env vars)
#    -> database_url for postgres (postgres://lcnocbrmucvymo:8c0cf06f1c8f797032d638c03169f309623bb92ea80d1dc61febc8bbe4c7b1b1@ec2-52-3-60-53.compute-1.amazonaws.com:5432/dahaea12a669hl )
#   go to pgadmin
#    -> right click server, create server
#    -> create database ("online database uri parsers" for help)
#    -> go to onew new database, you can see all sorts of databases we don't have access to
#    -> ours is dahaea12a669hl
#       -> there's the database, schema, tb1 and tb2 are example tables by Max
#       -> can right click, query tool, and execute on the data
#    -> put useful prepared statements into db.py

# don't touch deploy_heroku
# can try deploy_local, may not work
#   config.json holds all relevant data (copied data from heroku)
#   could get commit or auto-commit set on pgadmin

""" USERS FUNCTIONS """

# Set user information
def set_user(user_id, reddit_identity, fname, lname, gender, email, birthday):
    db = get_db()
    query = "INSERT INTO users (id, sub, fname, lname, gender, email, birthday) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    with db.cursor() as cursor:
        cursor.execute(query, (user_id, reddit_identity, fname, lname, gender, email, birthday))
        db.commit()
        cursor.close()

# Get user information
def get_user(user_id):
    db = get_db()
    query = "SELECT * FROM users WHERE id = %s LIMIT 1"
    with db.cursor() as cursor:
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        cursor.close()
    # Update last_accessed timestamp
    query = "UPDATE users SET last_accessed = NOW() WHERE id = %s"
    with db.cursor() as cursor:
        cursor.execute(query, (user_id,))
        db.commit()
        cursor.close()
    return user

# Get most recent users
def get_most_recent_users(limit = 10):
    db = get_db()
    query = "SELECT * FROM users ORDER BY last_accessed DESC LIMIT %s"
    with db.cursor() as cursor:
        cursor.execute(query, (limit,))
        users = cursor.fetchall()
        cursor.close()
    return users

# Get users by top total search history
def get_users_by_total_search_history(limit = 10):
    db = get_db()
    query = "SELECT users.id, users.fname, users.lname, COUNT(*) FROM users \
        LEFT JOIN search_history ON users.id = search_history.user_id \
            GROUP BY users.id ORDER BY count(*) DESC LIMIT %s" 
    with db.cursor() as cursor:
        cursor.execute(query, (limit,))
        users = cursor.fetchall()
        cursor.close()
    return users

# Get user privileges
def get_user_privileges(user_id):
    db = get_db()
    query = "SELECT level FROM privileges WHERE user_id = %s LIMIT 1"
    with db.cursor() as cursor:
        cursor.execute(query, (user_id,))
        privileges = cursor.fetchone()
        cursor.close()
    return privileges

""" SEARCH_HISTORY FUNCTIONS """

# Get search history by user
def get_user_search_history(user_id):
    db = get_db()
    query = "SELECT * FROM search_history WHERE user_id = %s"
    with db.cursor() as cursor:
        cursor.execute(query, (user_id,))
        search_history = cursor.fetchall()
        cursor.close()
    return search_history

# Add user search history
def add_user_search_history(user_id, search_term):
    db = get_db()
    query = "INSERT INTO search_history (user_id, search) VALUES (%s, %s)"
    with db.cursor() as cursor:
        cursor.execute(query, (user_id, search_term))
        db.commit()
        cursor.close()

# Get search history, sorted by most recent
def get_most_recent_search_history(limit = 10):
    db = get_db()
    query = "SELECT * FROM search_history ORDER BY last_accessed DESC LIMIT %s"
    with db.cursor() as cursor:
        cursor.execute(query, (limit,))
        search_history = cursor.fetchall()
        cursor.close()
    return search_history

''' INTERESTS FUNCTIONS '''
# Get all unique interests
def get_all_interests():
    db = get_db()
    query = "SELECT DISTINCT interest, description FROM interests"
    with db.cursor() as cursor:
        cursor.execute(query)
        interests = cursor.fetchall()
        cursor.close()
    return interests

# Add interest
def add_interest(interest, description = None):
    db = get_db()
    if description is None:
        query = "INSERT INTO interests (interest) VALUES (%s)"
    else:
        query = "INSERT INTO interests (interest, description) VALUES (%s, %s)"
    with db.cursor() as cursor:
        cursor.execute(query, (interest, description))
        db.commit()
        cursor.close()

# Add user interests
def add_user_interests(user_id, interests):
    db = get_db()
    interest_query = "SELECT id FROM interests WHERE interest = %s LIMIT 1"
    query = "INSERT INTO user_interests (user_id, interest) VALUES (%s, %s)"
    interests_ids = []
    with db.cursor() as cursor:
        for interest in interests:
            cursor.execute(interest_query, (interest,))
            interest_id = cursor.fetchall()
            cursor.execute(query, (user_id, interest_id))
        db.commit()
        cursor.close()

""" DATABASE FUNCTIONS """

# Initialize the database on click
@click.command('init-db')
@with_appcontext
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        with db.cursor() as cursor:
            cursor.execute(f.read().decode('utf8'))
    
    click.echo('Initialized the database.')

# Close database connection
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)           # close on teardown
    app.cli.add_command(init_db)                # add init_db to click