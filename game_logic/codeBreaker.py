#!usr/bin/python3
""" CodeBreaker class """
from constants import GUESS_LENGTH, MAX_NUMBER_OF_GUESSES, PEG_COLORS, GUESS_PROMPT, USER_INPUT_ERROR_MSG, MISSING_INPUT_ERROR_CODE, UNKNOWN_COLOR_ERROR_CODE
import numpy as np

color_to_number = {
    'blue': 0,
    'purple': 1,
    'yellow': 2,
    'orange': 3,
    'green': 4,
    'black': 5
}

class CodeBreaker:

    def __init__(self):
        """ initializes an instance """
        pass

    def makeGuess_notest(self, guessCount):

        return np.array(input(GUESS_PROMPT).split(), dtype=int)

    def makeGuess(self, guessCount):
        """ returns a validated guess """
        guessesLeft = MAX_NUMBER_OF_GUESSES - guessCount
        print('\nNumber of guesses left: {}'.format(guessesLeft))

        guess = np.array(input(GUESS_PROMPT).split(), dtype=int)
        
        inputValidationResult = self._validateUserInput(guess)
        print(inputValidationResult)
        self._printUserFriendlyErrorMessage(inputValidationResult)

        while inputValidationResult is not None:
            guess_str = input(GUESS_PROMPT).split()
            guess = np.array([color_to_number[color]
                              for color in guess_str if color in color_to_number])
            inputValidationResult = self._validateUserInput(guess)
            self._printUserFriendlyErrorMessage(inputValidationResult)
        return guess



    def _validateUserInput(self, guess):
        """ validates user input """
        if len(guess) != GUESS_LENGTH:
            return MISSING_INPUT_ERROR_CODE
        for num in guess:
            if num not in PEG_COLORS:  # assuming PEG_COLORS is now an array of numbers
                return UNKNOWN_COLOR_ERROR_CODE
        return None



    def _printUserFriendlyErrorMessage(self, errCode):
        """ prints error messages based on user input """
        if errCode == MISSING_INPUT_ERROR_CODE:
            print('Please enter 4 colors.')
            print(USER_INPUT_ERROR_MSG)
        elif errCode == UNKNOWN_COLOR_ERROR_CODE:
            print('Wrong color provided.')
            print(USER_INPUT_ERROR_MSG)
        else:  # assume None
            return
