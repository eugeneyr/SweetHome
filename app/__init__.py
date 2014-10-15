from flask import Flask
from flask.ext.bootstrap import Bootstrap
from app.life import life

bootstrap = None

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.register_blueprint(life.life)
    return app


