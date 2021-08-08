from flask import render_template, request
from app import app
from models.game import *
from models.player import *

@app.route('/game')
def index():
    return render_template("index.html", games=games)

# @app.route('/game/<choice>', methods=['POST'])
# def add_player():
#     player_name = request.form['name']
#     player_choice = request.form['choice']
#     new_task = Player(choice)
#     player_choice(new_task)
#     return render_template('index.html', name='name',choice='choice', games=games)