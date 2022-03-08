from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


login_manager = LoginManager()
login_manager._session_protection ='strong'
login_manager.login_view = 'auth.login'


db = SQLAlchemy()





bootstrap = Bootstrap()

app =Flask(__name__,instance_relative_config=True)

app.config.from_object(DevConfig)

bootstrap.init_app(app)
db.init_app(app)

from app import views

# login_manager.init_app(app)


    
    


  
# from flask import Flask
# from config import DevConfig
# from flask_bootstrap import Bootstrap



# app =Flask(__name__, instance_relative_config=True)

# Bootstrap(app)

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')


# from app import views


# bootstrap = Bootstrap()


