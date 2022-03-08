from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail



from flask_login import LoginManager


login_manager = LoginManager()
login_manager._session_protection ='strong'
login_manager.login_view = 'auth.login'


db = SQLAlchemy()
mail = Mail()




bootstrap = Bootstrap()

app =Flask(__name__,instance_relative_config=True)

app.config.from_object(DevConfig)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD =os.environ.get("mail_password")


bootstrap.init_app(app)
db.init_app(app)
mail.init_app(app)




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


