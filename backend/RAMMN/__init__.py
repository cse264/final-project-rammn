import os

import json

from flask import Flask

from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    config_path = os.path.join(os.getcwd(), "config.json")

    if os.path.exists(config_path):
        app.config.from_file(config_path, load=json.load)
        print(app.config["GOOGLE_OAUTH"]["client_id"])
    else:
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.environ['DATABASE_URL'],
        )

    Cors = CORS(app)

    CORS(app, resources={r'/*': {'origins': '*'}},
         CORS_SUPPORTS_CREDENTIALS=True)

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

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from .views import sample_page

    app.register_blueprint(sample_page, url_prefix='/')

    return app


app = create_app()
