from django.test import TestCase
from modelsTdd import kata1

"""
1. You are not allowed to write any production code unless it is to make a failing unit test
pass.

2. You are not allowed to write any more of a unit test than is sufficient to fail, and
compilation failures are failures.

3. You are not allowed to write any more production code than is sufficient to pass the one
failing unit test.

Red --> Green --> Reflect --> Refactor

Fake it green bar pattern
"""

class RockPaperScissorsTest(TestCase):
    """This class tests the rock paper scissors function in kata 1"""

    def setUp(self):
        """Set up common values before each test."""
        self.moves = ("Rock", "Paper", "Scissors")
        self.results = ("Player1 wins!", "Player2 wins!", "Tie!")
        self.systemUnderTest = kata1.createRockPaperScissors


    def test_rock_paper_scissors_scenarios_rock(self):
        """Test all possible RPS scenarios using a loop for rock."""
        test_cases = [
            (self.moves[0], self.moves[2], self.results[0]),  # Rock vs Scissors -> Player1 wins
            (self.moves[0], self.moves[1], self.results[1]),  # Rock vs Paper -> Player2 wins
            (self.moves[0], self.moves[0], self.results[2]),  # Rock vs Rock -> Tie
        ]

        for player1, player2, expected in test_cases:
            with self.subTest(player1=player1, player2=player2):
                self.assertEqual(self.systemUnderTest(player1, player2), expected)

    def test_rock_paper_scissors_scenarios_paper(self):
        """Test all possible RPS scenarios using a loop for paper."""
        test_cases = [
            (self.moves[1], self.moves[0], self.results[0]),  # Paper vs Rock -> Player1 wins
            (self.moves[1], self.moves[2], self.results[1]),  # Paper vs Scissors -> Player2 wins
            (self.moves[1], self.moves[1], self.results[2]),  # Paper vs Paper -> Tie
        ]

        for player1, player2, expected in test_cases:
            with self.subTest(player1=player1, player2=player2):
                self.assertEqual(self.systemUnderTest(player1, player2), expected)

    def test_rock_paper_scissors_scenarios_scissors(self):
        """Test all possible RPS scenarios using a loop for scissors."""
        test_cases = [
            (self.moves[2], self.moves[1], self.results[0]),  # Scissors vs Paper -> Player1 wins
            (self.moves[2], self.moves[0], self.results[1]),  # Scissors vs Rock -> Player2 wins
            (self.moves[2], self.moves[2], self.results[2]),  # Scissors vs Scissors -> Tie
        ]

        for player1, player2, expected in test_cases:
            with self.subTest(player1=player1, player2=player2):
                self.assertEqual(self.systemUnderTest(player1, player2), expected)