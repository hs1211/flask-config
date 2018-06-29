from flask import Flask

from app.about.controller import main
from app.config import configure_app


app = Flask(__name__)

# Middleware
configure_app(app)

# Route
app.register_blueprint(main, url_prefix='/')
