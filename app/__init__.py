from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app import views
from flask_login import LoginManager


login_manager = LoginManager()
login_manager._session_protection ='strong'
login_manager.login_view = 'auth.login'

Bootstrap()
db = SQLAlchemy()






bootstrap = Bootstrap()

def initializer(config_name):
    app =Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options)

    bootstrap.init_app()
    db.init_app(app)

    login_manager.init_app(app)
    


  

