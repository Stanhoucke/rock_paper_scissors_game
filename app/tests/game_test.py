import unittest
from app.classes.game import Game
from app.classes.player import Player

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("David", "Rock")
        self.player_2 = Player("Emma", "Paper")
        self.player_3 = Player("Fred", "Scissors")

        self.game = Game()

        self.choice_list = ["rock", "paper", "scissors"]

    # Tests for play method
    def test_play__rock_beats_scissors(self):
        self.assertEqual("Player 1 wins by playing rock!", self.game.play(self.player_1.choice, self.player_3.choice))

    def test_play__paper_beats_rock(self):
        self.assertEqual("Player 1 wins by playing paper!", self.game.play(self.player_2.choice, self.player_1.choice))

    def test_play__scissors_beat_paper(self):
        self.assertEqual("Player 1 wins by playing scissors!", self.game.play(self.player_3.choice, self.player_2.choice))

    def test_play__return_tie(self):
        self.assertIsNone(self.game.play(self.player_2.choice, self.player_2.choice))

    def test_play__scissors_loses_to_rock(self):
        self.assertEqual("Player 2 wins by playing rock!", self.game.play(self.player_3.choice, self.player_1.choice))

    def test_play__rock_loses_to_paper(self):
        self.assertEqual("Player 2 wins by playing paper!", self.game.play(self.player_1.choice, self.player_2.choice))

    def test_play__paper_loses_to_scissors(self):
        self.assertEqual("Player 2 wins by playing scissors!", self.game.play(self.player_2.choice, self.player_3.choice))

    def test_play__invalid_player_1_choice(self):
        # Assign invalid choice to player
        self.player_1.choice = "Lizard"
        message = "One of the players didn't choose 'rock', 'paper', or 'scissors', please check your spelling and try again."
        self.assertEqual(message, self.game.play(self.player_1.choice, self.player_2.choice))
    
    def test_play__invalid_player_2_choice(self):
        # Assign invalid choice to player
        self.player_2.choice = "Spock"
        message = "One of the players didn't choose 'rock', 'paper', or 'scissors', please check your spelling and try again."
        self.assertEqual(message, self.game.play(self.player_1.choice, self.player_2.choice))

    # Tests for computer choice method
    def test_computer_choice__returns_valid_option(self):
        self.assertTrue(self.game.computer_choice() in self.choice_list)

    # Tests for play using computer choice
    def test_play_against_computer__returns_valid_winner(self):
        computer_choice = self.game.computer_choice()
        if computer_choice == "rock":
            self.assertEqual(None, self.game.play(self.player_1.choice, computer_choice))
        elif computer_choice == "paper":
            self.assertEqual("Player 2 wins by playing paper!", self.game.play(self.player_1.choice, computer_choice))
        elif computer_choice == "scissors":
            self.assertEqual("Player 1 wins by playing rock!", self.game.play(self.player_1.choice, computer_choice))
