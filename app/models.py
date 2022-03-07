from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User:
    '''
    class that handles the user infomation
    '''
    __table__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    def __repr__(self):
        return f'User {self.username}'