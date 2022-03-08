from .models import User
from .form import RegistrationForm
from flask import render_template, request, url_for
from . import app





@app.route('/')
def index():

    return render_template('index.html')


@app.route("/register")
def register():
    Registration= RegistrationForm()

    return render_template('form.html', Registration=RegistrationForm)

@app.route('/success', methods=['post'])
def success():
    return render_template('success.html')
