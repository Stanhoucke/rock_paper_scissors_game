from flask import render_template, request
from app import app
from app.classes.player import Player
from app.classes.game import Game


@app.route("/")
def index():
    return "Hello, world!"