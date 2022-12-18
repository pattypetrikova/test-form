from flask import Blueprint, render_template, request, flash
from flask_mail import Message
from . import  mail

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():

    if request.method != "POST":
        return render_template("index.html")

    name = request.form.get("name")
    company = request.form.get("company")
    email = request.form.get("email")
    phone = request.form.get("phone")
    subject = request.form.get("subject")
    text = request.form.get("text")

    if len(name) < 3:
        flash("Name must have at least 3 characters", category="error")

    msg = Message(subject, sender="me@example.com", recipients=["pepa.cer18@gmail.com"])
    msg.body = \
f'''
{text}

{name}
{phone}
{email}
{company}
'''
    mail.send(msg)

    return render_template("index.html")


