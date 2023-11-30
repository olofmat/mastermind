#!usr/bin/python3
""" CodeBreaker class """
from constants import *


class CodeBreaker:

    def __init__(self):
        """ initializes an instance """
        pass


    def makeGuess(self, guessCount):
        """ returns a validated guess """
        guessesLeft = MAX_NUMBER_OF_GUESSES - guessCount
        print('\nNumber of guesses left: {}'.format(guessesLeft))
        guess = input(GUESS_PROMPT).split()
        inputValidationResult = self._validateUserInput(guess)
        self._printUserFriendlyErrorMessage(inputValidationResult)
        while inputValidationResult is not None:
            guess = input(GUESS_PROMPT).split()
            inputValidationResult = self._validateUserInput(guess)
            self._printUserFriendlyErrorMessage(inputValidationResult)
        return guess


    def _validateUserInput(self, guess):
        """ validates user input """
        if 'exit' in guess:
            print('Goodbye...')
            quit()
        if len(guess) != GUESS_LENGTH:
            return MISSING_INPUT_ERROR_CODE
        for color in guess:
            if color not in PEG_COLORS:
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
