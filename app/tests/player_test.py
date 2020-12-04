import unittest
from app.classes.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("David", "Rock")
        self.player_2 = Player("Emma", "Paper")
        self.player_3 = Player("Fred", "Scissors")

    def test_player_has_name(self):
        self.assertEqual("David", self.player_1.name)

    def test_player_choice__returns_rock(self):
        choice = self.player_1.choice
        self.assertEqual("Rock", choice)

    def test_player_choice__returns_paper(self):
        choice = self.player_1.choice = "Paper"
        self.assertEqual("Paper", choice)

    def test_player_choice__returns_scissors(self):
        choice = self.player_1.choice = "Scissors"
        self.assertEqual("Scissors", choice)