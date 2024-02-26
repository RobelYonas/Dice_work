import unittest
from Game import games

class TestGames(unittest.TestCase):

    def setUp(self):
        self.game = games(['Player 1', 'Player 2'])

    def test_game_initialization(self):
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.players[0].name, 'Player 1')
        self.assertEqual(self.game.players[1].name, 'Player 2')

if __name__ == '__main__':
    unittest.main()
