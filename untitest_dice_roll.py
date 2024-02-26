import unittest
from unittest.mock import patch
import random
from dice_roll import Die


class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Die()

    def test_roll(self):
        with patch.object(random, 'randint', return_value=3):
            self.assertEqual(self.die.roll(), 3)


if __name__ == '__main__':
    unittest.main()
