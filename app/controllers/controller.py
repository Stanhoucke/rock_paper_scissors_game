from flask import render_template, request
from app import app
from app.classes.player import Player
from app.classes.game import Game

game = Game()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<player_1_choice>/<player_2_choice>")
def play_game(player_1_choice, player_2_choice):
    return game.play(player_1_choice, player_2_choice)