'''
    CS 5001, Fall 2023
    Final Project -- Mastermind
    Yifan Chen

    This is the GameLogic class.
'''
import random

class GameLogic:
    '''
    This class has one method that represents the logic for 
    evaluating the guesses in the Mastermind game.

    Attributes:
        answers (list) -- a list containing player's guessed colors
    '''
    def __init__(self, answers=None):
        '''
        Constructor -- create a new GameLogic instance
        Parameter:
            self -- the current object
            answers -- player's guesses list
        Attributes: 
        '''
        if answers is  None:
            answers = []
        self.answers = answers

    def check_result(self, code):
        '''
        Method: check_result
            Compare player's answers with the code, and create a list
            of scoring pegs to represent the result
        Parameters:
            self -- the current object
            code -- the secret code to be compared with
        Returns the scoring pegs list
        '''
        correct_guess = 'black'
        half_correct_guess = 'red'
        scoring_pegs = []
        
        # check the result only when the length of answers is 4
        if len(self.answers) != 4:
            return
        else:       
            for i in range(4):
                if self.answers[i] == code[i]:
                    scoring_pegs.append(correct_guess)
                elif self.answers[i] in code:
                    scoring_pegs.append(half_correct_guess)

        # scoring pegs are placed in random order
        random.shuffle(scoring_pegs)

        # adding empty pegs to scoring_pegs until its length is 4
        while len(scoring_pegs) < 4:
            scoring_pegs.append('')

        return scoring_pegs
