from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app import views




Bootstrap()
db = SQLAlchemy()






bootstrap = Bootstrap()

def initializer(config_name):
    app =Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options)

    bootstrap.init_app()
    db.init_app(app)
    

  

