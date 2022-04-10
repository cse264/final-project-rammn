from lib2to3.pytree import _Results
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

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:

        with db.cursor() as cursor:
            cursor.execute(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)