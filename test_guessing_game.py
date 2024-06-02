import unittest
from unittest.mock import patch
from guessing_game import guess_number  # Adjust the imporcd destopt as needed


class GuessNumberTest(unittest.TestCase):

    @patch('random.randint', return_value=10)
    def test_correct_guess(self, mock_randint):
        secret_number = 10
        guesses = [10]
        result = guess_number(secret_number, guesses)
        self.assertIn("congratulation you won", result)

    @patch('random.randint', return_value=10)
    def test_all_guesses_too_high(self, mock_randint):
        secret_number = 10
        guesses = [15, 14, 13]
        result = guess_number(secret_number, guesses)
        self.assertIn("value too high try again", result)
        self.assertIn("oh sorry you failed all try attempt", result)

    @patch('random.randint', return_value=10)
    def test_all_guesses_too_low(self, mock_randint):
        secret_number = 10
        guesses = [1, 2, 3]
        result = guess_number(secret_number, guesses)
        self.assertIn("value too low try again", result)
        self.assertIn("oh sorry you failed all try attempt", result)

    @patch('random.randint', return_value=10)
    def test_mixed_guesses(self, mock_randint):
        secret_number = 10
        guesses = [5, 15, 10]
        result = guess_number(secret_number, guesses)
        self.assertIn("value too low try again", result)
        self.assertIn("value too high try again", result)
        self.assertIn("congratulation you won", result)


if __name__ == "__main__":
    unittest.main()
