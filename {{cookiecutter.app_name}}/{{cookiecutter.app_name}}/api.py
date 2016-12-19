# coding: utf-8

import flask
import flask_restful

from {{cookiecutter.app_name}}.extensions import auth


class LoggedInResource(flask_restful.Resource):
    method_decorators = [auth.login_required]


class HelloWorld(LoggedInResource):
    def get(self):
        return {'hello': 'world'}


def register_api(app):
    api = flask_restful.Api()

    @api.representation('application/json')
    def output_json(data, code, headers=None):
        response = flask.make_response(flask.json.dumps(data), code)
        response.headers.extend(headers or {})
        return response

    api.add_resource(HelloWorld, '/')
    api.init_app(app)
