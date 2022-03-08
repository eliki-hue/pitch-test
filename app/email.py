import imp
from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(username):
    sender_email = 'eliki13720@gmail.com'
    subject= 'Welcome to pitch_test'
    email = Message(subject=subject, sender=sender_email, recipients=username)
    email.body = '''
    Hello {{username}},
    We have noticed that you have registered to pitch_test. Welcome and have fun creating your 1 minute pitch and seeing other peoples pitch_test

    '''
   
    mail.send(email)
