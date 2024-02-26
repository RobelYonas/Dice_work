import unittest

from Player2 import player2

class TestPlayer(unittest.TestCase):
    def test_add_score(self):
        p = player2("Alice")
        p.add_score(10)
        self.assertEqual(p.score, 10)
        
    def test_reset_score(self):
        p = player2("Bob")
        p.add_score(20)
        p.reset_score()
        self.assertEqual(p.score, 0)

if __name__ == '__main__':
    unittest.main()
