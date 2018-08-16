from flask import Flask

from app.api.v1 import create_blueprint
from app.modles.base import db
from app.libs.custom_response import MyResponse


def register_blueprints(app):
    app.register_blueprint(create_blueprint(), url_prefix='/api/v1')


def register_plugin(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.response_class = MyResponse
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    register_plugin(app)

    return app
