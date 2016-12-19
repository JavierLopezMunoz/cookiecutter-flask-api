# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('{{cookiecutter.app_name | upper}}_SECRET', 'secret-key')
    APP_NAME = '{{cookiecutter.app_name}}'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    # Flask-HTTPAuth config
    HTTPAUTH = (
        os.environ.get('{{cookiecutter.app_name | upper}}_HTTPAUTH_USERNAME', 'admin'),
        os.environ.get('{{cookiecutter.app_name | upper}}_HTTPAUTH_PASSWORD', 'admin')
    )


class DevelopmentConfig(Config):
    """Development configuration."""

    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""

    ENV = 'production'
    DEBUG = False
