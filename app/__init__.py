from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)
talisman = Talisman(app, content_security_policy=None)

from app import views
