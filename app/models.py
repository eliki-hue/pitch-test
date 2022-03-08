from unicodedata import category
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(db.Model):
    '''
    class that handles the user infomation
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password= db.Column(db.String(255))

    def __init__(self, username,email,password):
        self.username= username
        self.email=email
        self.password=password 

    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')

    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)

    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)

    # from . import login_manager

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key= True)
    category =db.Column(db.String(255))
    sender = db.Column(db.String(255))
    pitch =db.column(db.String())




    def __repr__(self):
        return f'User {self.username}'