from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
mail = Mail(app)

from app import routes, errors
