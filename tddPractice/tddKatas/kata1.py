"""This file will allow me to practice TDD"""

def createRockPaperScissors(p1Move, p2Move):
    """This function takes in moves for both players and outputs winner"""
    moves = ("Rock","Paper","Scissors")
    results = ("Player1 wins!", "Player2 wins!", "Tie!")

    # Predefined scenarios
    scenarios = [
        {"p1Move": moves[1], "p2Move": moves[0], "response": results[0]},  # Paper vs Rock -> Player1 wins
        {"p1Move": moves[1], "p2Move": moves[2], "response": results[1]},  # Paper vs Scissors -> Player2 wins
        {"p1Move": moves[0], "p2Move": moves[2], "response": results[0]},  # Rock vs Scissors -> Player1 wins
        {"p1Move": moves[0], "p2Move": moves[1], "response": results[1]},  # Rock vs Paper -> Player2 wins
        {"p1Move": moves[2], "p2Move": moves[1], "response": results[0]},  # Scissors vs Paper -> Player1 wins
        {"p1Move": moves[2], "p2Move": moves[0], "response": results[1]},  # Scissors vs Rock -> Player2 wins
        {"p1Move": moves[0], "p2Move": moves[0], "response": results[2]},  # Rock vs Rock -> Tie
        {"p1Move": moves[1], "p2Move": moves[1], "response": results[2]},  # Paper vs Paper -> Tie
        {"p1Move": moves[2], "p2Move": moves[2], "response": results[2]},  # Scissors vs Scissors -> Tie
    ]

    # Check for predefined scenarios
    for scenario in scenarios:
        if scenario["p1Move"] == p1Move and scenario["p2Move"] == p2Move:
            return scenario["response"]

    # if p1Move == moves[1] and p2Move == moves[2]:
    #     # if player 1 is paper and player 2 is scissors
    #     return results[1]

    # elif p1Move == moves[0] and p2Move == moves[2]:
    #     # if player 1 is rock and player 2 is scissors
    #     return results[0]

    # elif p1Move == moves[0] and p2Move == moves[1]:
    #     # if player 1 is rock and player 2 is paper
    #     return results[1]

    # elif p1Move == moves[2] and p2Move == moves[0]:
    #     # if player 1 is scissors and player 2 is rock
    #     return results[1]

    # elif p1Move == p2Move:
    #     # if player 1 is equal to player 2 move
    #     return results[2]

    # return results[0]