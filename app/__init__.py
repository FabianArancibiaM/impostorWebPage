from flask import Flask, g
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth
from .db_service import init_db


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    init_db()
    return app

