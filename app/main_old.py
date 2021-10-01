from decouple import config as config_decouple
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        # db.create_all()

    return app


db = SQLAlchemy()
enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

app = create_app(enviroment)
