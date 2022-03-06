from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy





Bootstrap(app)
db = SQLAlchemy()






bootstrap = Bootstrap()

def initializer(config_name):
    app =Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options)

    from app import views
