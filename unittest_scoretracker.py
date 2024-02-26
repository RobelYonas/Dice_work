
import unittest
from io import StringIO
from contextlib import redirect_stdout
from scoretracker import scoreboard

class TestScoreboard(unittest.TestCase):

    def test_display_scoreboard_prints_scores(self):
        player_names = ['Alice', 'Bob', 'Charlie']
        sb = scoreboard(player_names)
        sb.scores = {'Alice': 100, 'Bob': 50, 'Charlie': 75}
        with redirect_stdout(StringIO()) as output:
            sb.display_scoreboard()
        self.assertEqual(output.getvalue().strip(), "Current scores:\nAlice: 100\nBob: 50\nCharlie: 75")


if __name__ == '__main__':
    unittest.main()
