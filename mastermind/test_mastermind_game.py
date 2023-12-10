'''
    CS 5001, Fall 2023
    Final Project -- Mastermind
    Yifan Chen

    This is the TestGame class to test the game logic.
'''
import unittest
from GameLogic import GameLogic

class TestGame(unittest.TestCase):
    '''
    Test the check_result method in the GameLogic class
    '''
    def test_check_result(self):
        # first test
        game1 = GameLogic()
        game1.answers = ["green", "red", "blue", "yellow"]
        code1 = ["blue", "black", "purple", "red"]

        scoring_pegs1 = game1.check_result(code1)
        # black indicates correct color and correct placement
        expect_black1 = 0
        # red indicates correct color but incorrect placement
        expect_red1 = 2

        actual_black1 = scoring_pegs1.count("black")
        actual_red1 = scoring_pegs1.count("red")

        self.assertEqual(expect_black1, actual_black1)
        self.assertEqual(expect_red1, actual_red1)

        # second test
        game2 = GameLogic()
        game2.answers = ["black", "red", "blue", "yellow"]
        code2 = ["green", "black", "blue", "purple"]

        scoring_pegs2 = game2.check_result(code2)
        expect_black2 = 1
        expect_red2 = 1

        actual_black2 = scoring_pegs2.count("black")
        actual_red2 = scoring_pegs2.count("red")

        self.assertEqual(expect_black2, actual_black2)
        self.assertEqual(expect_red2, actual_red2)       

if __name__ == "__main__":
    unittest.main(verbosity=3)