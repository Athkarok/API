import os
from app import mail
from flask import render_template
from flask_mail import Message


class MailAdmin:
    
    def send(self, title, message, recips):
        msg = Message(title, sender=("Athkarok App", os.environ.get("M_USER")), recipients= recips)
        msg.body = message
        try:
            mail.send(msg)
        except:
            print(f"Error: Email with title {title} mesage: {message}  recipients: {recips} has not been sent.")
 
    def send_template(self, temp_name, title, message, recips):
        msg = Message(title, sender=("Athkarok App", os.environ.get("M_USER")), recipients= recips)
        msg.html = render_template(temp_name, text= message)
        try:
            mail.send(msg)
        except:
            print(f"Error: Email with title {title} mesage: {message}  recipients: {recips} has not been sent.")

