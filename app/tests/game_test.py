import unittest

from app.models.game import Game  # *
from app.models.player import Player  # *

class TestGame(unittest.TestCase):
    def setUp(self):
        # setup go here
        pass
    
    def test_player_1_wins(self):
        # test rock beats scissors
        # test goes here
        self.assertEqual(True, True)