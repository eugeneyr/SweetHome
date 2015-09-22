from flask import Blueprint, render_template

game = Blueprint('game', __name__)

@game.route('/game')
def main():
    return render_template('sixteen/game.html')