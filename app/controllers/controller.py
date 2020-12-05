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
    result = game.play(player_1_choice, player_2_choice)
    return render_template("result.html", player_1_choice = player_1_choice, player_2_choice = player_2_choice, result = result)

@app.route("/play", methods=["GET", "POST"])
def play_computer():

    if request.method == "GET":
        return render_template("play.html")

    else:
        player_1 = Player(request.form["name"], request.form["choice"])
        computer_choice = game.computer_choice()
        result = game.play(player_1.choice, computer_choice)
        return render_template("result.html", player_1_choice = player_1.choice, player_2_choice = computer_choice, result = result)
