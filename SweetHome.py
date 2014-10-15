# from flask import Flask, make_response, render_template
from flask.ext.script import Manager

from app import create_app

app = create_app()
#
# app = Flask(__name__)

manager = Manager(app)


#
#
# @app.route('/')
# def hello_world():
#     return render_template('ship_animation.html')
#
#
# @app.route('/ship')
# def ship():
#     return render_template('ship_animation.html')
#

if __name__ == '__main__':
    manager.run()
