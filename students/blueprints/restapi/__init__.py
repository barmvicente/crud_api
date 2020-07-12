from flask import Blueprint
from flask_restful import Api

from .resources import (
    StudentResource,
    StudentInsertResource
)

bp = Blueprint("restapi", __name__)
api = Api(bp)


def init_app(app):
    api.add_resource(StudentResource, "/")
    api.add_resource(StudentInsertResource, "/insert/")
    app.register_blueprint(bp)
    