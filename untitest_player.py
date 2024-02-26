import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_update_name(self):
        p = Player("John")
        p.update_name("Jane")
        self.assertEqual(p.name, "Jane")

if __name__ == '__main__':
    unittest.main()
