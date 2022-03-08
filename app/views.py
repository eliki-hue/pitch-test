
from .models import User
from .form import RegistrationForm
from flask import render_template, request, url_for
from . import app, db



@app.route('/')
def index():

    return render_template('index.html')


@app.route("/register")
def register():
    Registration= RegistrationForm()
    

    return render_template('form.html', Registration=RegistrationForm)

@app.route('/success', methods=['GET','POST'])
def success():
    if request.method == "POST":

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('psw')
        print(username)
        print(email)
        print(password)
        data = User(username,email,password)

        db.session.add(data)
        db.session.commit()

    return render_template('success.html')
    
