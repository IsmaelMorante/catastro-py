from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify
import os

db = SQLAlchemy()


def page_not_found(e):
    print('Error', e)
    return redirect(url_for('main.index'))


def create_app():
    app = Flask(__name__, static_url_path='/static')
    is_prod = os.environ.get('PRODUCTION', None)
    if is_prod:
        app.config.from_object("app.config.ProductionConfig")
    else:
        app.config.from_object("app.config.DevelopmentConfig")

    db.init_app(app)
    with app.app_context():
        from app.models import Test
        db.create_all()
        db.session.commit()

    sslify = SSLify(app, subdomains=True)
    app.register_error_handler(500, page_not_found)
    app.register_error_handler(404, page_not_found)

    # blueprint for auth routes in our app
    # from blueprints.auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from app.blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # login_manager = LoginManager(app)
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # from models import User
    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    return app


app = create_app()
