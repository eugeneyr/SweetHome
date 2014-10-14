from flask import Blueprint, render_template

life = Blueprint('life', __name__)

@life.route('/life')
def main():
    return render_template('life/main.html')