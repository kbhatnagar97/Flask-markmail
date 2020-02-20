from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('/home/kshitij_bhatnagar/apps/Python/markmail/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


app = create_app(config_name="config")

app.debug = True
db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db)

from app import routes, models
