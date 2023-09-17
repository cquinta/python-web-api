from flask import Flask
from blog.config import configure

def create_app():
    app = Flask(__name__)
    configure(app)
    return app





