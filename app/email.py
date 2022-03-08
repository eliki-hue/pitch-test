import imp
from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(Subject, template,to, **kwargs):
    sender_email = 'eliki13720@gmail.com'
    email = Message(subject='', sender=sender_email, recipients=[])
    email.body =render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)
    