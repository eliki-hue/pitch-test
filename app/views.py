from .email import mail_message
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
        if db.session.query(User).filter(User.email ==email).count()==0:

            print(username)
            print(email)
            print(password)
            data = User(username,email,password)

            db.session.add(data)
            db.session.commit()
            try:
                mail_message(username)
            except:
                pass
            return render_template('success.html')
    
        return render_template('form.html', text ='User with that email address already exist')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/profile')
def profile():
    if request.method == "POST":

       
        email = request.form.get('email')
        password = request.form.get('psw')
        if db.session.query(User).filter(User.email ==email & User.password==password).count()==1:
           userProfile = db.session.query(User).filter(User.email ==email)

        return render_template('profile.html', profile =userProfile)

            
