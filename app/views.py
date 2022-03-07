from flask import render_template, request
from app import myapp





@myapp.route('/')
def index():
    heading = 'WELCOME TO MY APP'
    render_template('index.html',heading =heading)
