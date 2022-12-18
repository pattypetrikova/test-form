from flask import Flask
from flask_mail import Mail
import os

mail = Mail()

def create_app() -> Flask:

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "somekey"

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.environ.get('GMAIL_PW')
    app.config['MAIL_PASSWORD'] = os.environ.get('GMAIL_PW')
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail.init_app(app)

    from .views import views
    app.register_blueprint(views) # type: ignore

    return app
