from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


login_manager = LoginManager()
login_manager._session_protection ='strong'
login_manager.login_view = 'auth.login'


myapp =Flask(__name__)

db = SQLAlchemy(myapp)






bootstrap = Bootstrap()
bootstrap.init_app(myapp)

# def initializer(config_name):
#     myapp =Flask(__name__)
    
#     myapp.config.from_object(config_options[config_name])

#     bootstrap.init_app(myapp)
#     db.init_app(myapp)

#     from app import views
#     # login_manager.init_app(app)


#     return myapp

# def create_app():
#     app = Flask(__name__)

#     with app.app_context():
#         db.init_app(app)

#     return app


  

