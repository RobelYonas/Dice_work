import unittest
from Game2 import games2


class TestGame2(unittest.TestCase):
    def test_game_play(self):
        game = games2()
        game.game_play('easy')


if __name__ == '__main__':
    unittest.main()
