#!usr/bin/python3
""" CodeMaker class """
from constants import *
import random
import numpy as np

PEG_COLORS = np.arange(0, 6)


class CodeMaker:

    def __init__(self):
        """ initializes an instance """
        pass


    def createRandomCode(self):
        """ creates a code using random """
        np.random.seed(2)
        code = np.array(np.random.choice(PEG_COLORS, CODE_LENGTH))
        print(code)
        return code


    def createCode(self): 
        """ returns a validated code """
        code = input(CODE_PROMPT).split()
        inputValidationResult = self._validateUserInput(code)
        self._printUserFriendlyErrorMessage(inputValidationResult)
        while inputValidationResult is not None:
            code = input(CODE_PROMPT).split()
            inputValidationResult = self._validateUserInput(code)
            self._printUserFriendlyErrorMessage(inputValidationResult)
        
        return code


    def _validateUserInput(self, code):
        """ validates user input """
        if 'exit' in code:
            print('Goodbye...')
            quit()
        if len(code) != GUESS_LENGTH:
            return MISSING_INPUT_ERROR_CODE
        for color in code:
            if color not in PEG_COLORS:
                return UNKNOWN_COLOR_ERROR_CODE
        return None

    def provideFeedback(self, codeToCopy, guessToCopy):
        """ provides feedback to code breaker """
        
        Feedback = np.array([0,0])
        code = np.array(codeToCopy)
        guess = np.array(guessToCopy)

        red_indices = np.where(guess == code)        
        Feedback[0] = len(red_indices[0])
        code[red_indices] = -1  # mark matched
        guess[red_indices] = -1  # mark matched

        # Check for color matches (WHITE)
        white_points = 0
        for i in range(CODE_LENGTH):
            if guess[i] != -1 and guess[i] in code:
                white_points += 1
                code[np.where(code == guess[i])[0][0]] = -1
        
        Feedback[1] = white_points
        
        return Feedback



    def _findFirstMatchedColor(self, codeToCopy, guessItem):
        """ finds the position of the first matched color """
        code = list(codeToCopy)
        for i in range(0, CODE_LENGTH):
            if code[i] == guessItem:
                return i


    def _checkWinnerStatus(self, feedback):
        """ returns the winning code if player won """
        if feedback[0] == 4:
            return True
        else:
            return False



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
