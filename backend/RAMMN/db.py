import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext

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




def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:

        with db.cursor() as cursor:     # close 
            cursor.execute(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# If db is already running, 
def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(current_app.config['DATABASE'])     # database url

    return g.db

# get_db()
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)