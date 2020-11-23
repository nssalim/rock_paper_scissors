import unittest

from app.models.player import Player
from app.models.game import Game

class TestPlayer(unittest.TestCase):

    def setUp(self):

        self.player = Player_1("Jack")
    

    def test_player_has_name(self):
        self.assertEqual(self, self.player.name)

