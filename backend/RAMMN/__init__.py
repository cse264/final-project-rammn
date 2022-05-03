import os

import json

from flask import Flask, session

from flask_session import Session

from flask_cors import CORS, cross_origin

from flask_caching import Cache

cache = Cache()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # check if config file is in current path
    config_path = os.path.join(os.getcwd(), "config.json")

    # check if config file exists
    if os.path.exists(config_path):
        # use config file to setup app configuration
        app.config.from_file(config_path, load=json.load)
    else:
        # setup default values for app configuration
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.environ['DATABASE_URL'],
            SESSION_PERMANENT=False,
            SESSION_TYPE="filesystem"
        )

    cache_servers = os.environ.get('MEMCACHIER_SERVERS')
    if cache_servers == None:
        cache.init_app(app, config={'CACHE_TYPE': 'simple'})
    else:
        cache_user = os.environ.get('MEMCACHIER_USERNAME') or ''
        cache_pass = os.environ.get('MEMCACHIER_PASSWORD') or ''
        cache.init_app(app,
                       config={'CACHE_TYPE': 'saslmemcached',
                               'CACHE_MEMCACHED_SERVERS': cache_servers.split(','),
                               'CACHE_MEMCACHED_USERNAME': cache_user,
                               'CACHE_MEMCACHED_PASSWORD': cache_pass,
                               'CACHE_OPTIONS': {'behaviors': {
                                   # Faster IO
                                   'tcp_nodelay': True,
                                   # Keep connection alive
                                   'tcp_keepalive': True,
                                   # Timeout for set/get requests
                                   'connect_timeout': 2000,  # ms
                                   'send_timeout': 750 * 1000,  # us
                                   'receive_timeout': 750 * 1000,  # us
                                   '_poll_timeout': 2000,  # ms
                                   # Better failover
                                   'ketama': True,
                                   'remove_failed': 1,
                                   'retry_timeout': 2,
                                   'dead_timeout': 30}}})


    with app.app_context():
        cache.clear()

    # set up CORS
    Cors = CORS(app)

    CORS(app, resources={r'/*': {'origins': '*'}},
         CORS_SUPPORTS_CREDENTIALS=True)

    # for testing purposes
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        app.config['CORS_HEADERS'] = 'Content-Type'
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # setup db
    from . import db
    db.init_app(app)

    # import reddit auth-routes
    from . import auth
    app.register_blueprint(auth.bp)

    # import user-routes
    from . import users
    app.register_blueprint(users.bp)

    # import interest-routes
    from . import interests
    app.register_blueprint(interests.bp)

    # get route responsible for serving main page
    from .views import sample_page
    app.register_blueprint(sample_page, url_prefix='/')

    return app


app = create_app()
