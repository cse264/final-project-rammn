import os

import json

from flask import Flask

from flask_cors import CORS, cross_origin

from backend.RAMMN.external_auth import RedditAuthenticator


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
        )

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

    # import auth-routes and register with app
    from . import auth
    app.register_blueprint(auth.bp)

    # get route responsible for serving main page
    from .views import sample_page
    app.register_blueprint(sample_page, url_prefix='/')

    return app


app = create_app()
