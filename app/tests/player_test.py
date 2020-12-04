import unittest
from app.classes.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("David")
        self.player_2 = Player("Emma")

    def test_player_has_name(self):
        self.assertEqual("David", self.player_1.name)

    def test_player_choice__returns_rock(self):
        choice = self.player_1.choice[0]
        self.assertEqual("Rock", choice)

    def test_player_choice__returns_paper(self):
        choice = self.player_1.choice[1]
        self.assertEqual("Paper", choice)

    def test_player_choice__returns_scissors(self):
        choice = self.player_1.choice[2]
        self.assertEqual("Scissors", choice)