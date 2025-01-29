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

# class RockPaperScissorsTest(TestCase):
#     """This clas will test the rock paper scissors kata"""

#     def setUp(self):
#         """This will contain the protocol to set up before every test in this class"""
#         self.moves = ("Rock", "Paper", "Scissors")
#         self.results = ("Player1 wins!", "Player2 wins!", "Tie!")

#     def tearDown(self):
#         """This will contain the protocol to clean up after every test in this class"""
#         pass

#     def test_player1_paper_and_player2_rock(self):
#         """Scenario 1 = Given that player 1 chooses paper and player 2 chooses rock - player 1 should win"""
#         # Arrage (state, services, systemUnderTest(sut))
#         expected = self.results[0]
#         player1Move = self.moves[1]
#         player2Move = self.moves[0]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_paper_and_player2_scissors(self):
#         """Scenario 2 = Given that player 1 chooses paper and player 2 chooses scissors - player 2 should win"""
#         # Arrage
#         expected = self.results[1]
#         player1Move = self.moves[1]
#         player2Move = self.moves[2]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_paper_and_player2_paper(self):
#         """Scenario 3 = Given that player 1 chooses paper and player 2 chooses paper - this should be a tie"""
#         # Arrange
#         expected = self.results[2]
#         player1Move = self.moves[1]
#         player2Move = self.moves[1]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_rock_and_player2_scissors(self):
#         """Scenario 4 = Given that player 1 chooses rock and player 2 chooses scissors - player 1 should win"""
#         # Arrange
#         expected = self.results[0]
#         player1Move = self.moves[0]
#         player2Move = self.moves[2]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_rock_and_player2_paper(self):
#         """Scenario 5 = Given that player 1 chooses rock and player 2 chooses paper - player 2 should win"""
#         # Arrange
#         expected = self.results[1]
#         player1Move = self.moves[0]
#         player2Move = self.moves[1]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_rock_and_player2_rock(self):
#         """Scenario 6 = Given that player 1 chooses rock and player 2 chooses rock - this should be a tie"""
#         # Arrange
#         expected = self.results[2]
#         player1Move = self.moves[0]
#         player2Move = self.moves[0]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_scissors_and_player2_paper(self):
#         """Scenario 7 = Given that player 1 chooses scissors and player 2 chooses paper - player 1 should win"""
#         # Arrange
#         expected = self.results[0]
#         player1Move = self.moves[2]
#         player2Move = self.moves[1]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_scissors_and_player2_rock(self):
#         """Scenario 8 = Given that player 1 chooses scissors and player 2 chooses rock - player 2 should win"""
#         # Arrange
#         expected = self.results[1]
#         player1Move = self.moves[2]
#         player2Move = self.moves[0]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_player1_scissors_and_player2_scissors(self):
#         """Scenario 9 = Given that player 1 chooses scissors and player 2 chooses scissors - this should be a tie"""
#         # Arrange
#         expected = self.results[2]
#         player1Move = self.moves[2]
#         player2Move = self.moves[2]
#         systemUnderTest = kata1

#         # Act
#         actual = systemUnderTest.createRockPaperScissors(player1Move, player2Move)

#         # Assert
#         self.assertEqual(actual, expected)

class RockPaperScissorsTest(TestCase):

    def setUp(self):
        """Set up common values before each test."""
        self.moves = ("Rock", "Paper", "Scissors")
        self.results = ("Player1 wins!", "Player2 wins!", "Tie!")
        self.systemUnderTest = kata1.createRockPaperScissors

    def test_rock_paper_scissors_scenarios(self):
        """Test all possible RPS scenarios using a loop."""
        test_cases = [
            (self.moves[1], self.moves[0], self.results[0]),  # Paper vs Rock -> Player1 wins
            (self.moves[1], self.moves[2], self.results[1]),  # Paper vs Scissors -> Player2 wins
            (self.moves[1], self.moves[1], self.results[2]),  # Paper vs Paper -> Tie
            (self.moves[0], self.moves[2], self.results[0]),  # Rock vs Scissors -> Player1 wins
            (self.moves[0], self.moves[1], self.results[1]),  # Rock vs Paper -> Player2 wins
            (self.moves[0], self.moves[0], self.results[2]),  # Rock vs Rock -> Tie
            (self.moves[2], self.moves[1], self.results[0]),  # Scissors vs Paper -> Player1 wins
            (self.moves[2], self.moves[0], self.results[1]),  # Scissors vs Rock -> Player2 wins
            (self.moves[2], self.moves[2], self.results[2]),  # Scissors vs Scissors -> Tie
        ]

        for player1, player2, expected in test_cases:
            with self.subTest(player1=player1, player2=player2):
                self.assertEqual(self.systemUnderTest(player1, player2), expected)