from flask import render_template, request
from app import app
from models.game import *
from models.player import *

@app.route("/")
def index():
    return render_template("index.html", games=games)

@app.route("/welcome")
def welcome_page():
    return render_template("welcome.html", games=games)

@app.route("/", methods=["POST"])
def add_choice():
    player_name = request.form["name"]
    player_choice = request.form["choice"]
    player_choice=Player(player_name, player_choice)
    return render_template('index.html', name="name",choice="choice", games=games)

@app.route("/Rock")
def first_choice():
    return render_template('first_selection.html', games=games)

@app.route("/Rock/Scissors")
def second_choice():
    return render_template("result.html", games=games)