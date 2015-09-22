from flask import Flask
from flask.ext.bootstrap import Bootstrap
from app.life import life
from app.sixteen import game

bootstrap = None

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.register_blueprint(life.life)
    app.register_blueprint(game.game)

    return app


