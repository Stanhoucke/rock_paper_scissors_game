import unittest
from app.classes.game import Game
from app.classes.player import Player

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("David", "Rock")
        self.player_2 = Player("Emma", "Paper")
        self.player_3 = Player("Fred", "Scissors")

    # def test_play__rock_beats_scissors(self):
    #     player_1_choice = self.player_1.choice[0]
    #     player_2_choice = self.player_2.choice[2]
    #     self.assertEqual("David wins!", play(player_1_choice, player_2_choice))