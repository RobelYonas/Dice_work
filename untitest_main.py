import unittest
import io
import sys

class TestMain(unittest.TestCase):

    def test_run_without_errors(self):
        # Redirect stdout to a StringIO object to capture output
        fake_output = io.StringIO()
        sys.stdout = fake_output

        try:
            import main  # Run the main script
        except Exception as e:
            self.fail(f"The code raised an exception: {e}")

        # Reset stdout
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
