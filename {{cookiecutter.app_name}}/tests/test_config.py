# -*- coding: utf-8 -*-
"""Test configs."""
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevelopmentConfig, ProductionConfig

def test_production_config():
    """Production config."""
    app = create_app(ProductionConfig)
    assert app.config['ENV'] == 'production'
    assert app.config['DEBUG'] is False


def test_dev_config():
    """Development config."""
    app = create_app(DevelopmentConfig)
    assert app.config['ENV'] == 'development'
    assert app.config['DEBUG'] is True
