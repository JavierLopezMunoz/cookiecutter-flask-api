"""The app module, containing the app factory function."""
import flask

from {{cookiecutter.app_name}} import commands
from {{cookiecutter.app_name}}.api import register_api
from {{cookiecutter.app_name}}.extensions import auth
from {{cookiecutter.app_name}}.settings import ProductionConfig


def create_app(config_object=ProductionConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = flask.Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_api(app)
    register_commands(app)
    return app


def register_extensions(app):
    # Flask-HTTPAuth
    @auth.get_password
    def get_pw(username):
        return dict([app.config.get('HTTPAUTH')]).get(username, None)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
