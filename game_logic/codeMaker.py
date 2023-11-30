#!usr/bin/python3
""" CodeMaker class """
from constants import *
import random


class CodeMaker:

    def __init__(self):
        """ initializes an instance """
        pass


    def createRandomCode(self):
        """ creates a code using random """
        code = []
        for peg in range(0, CODE_LENGTH):
            code.append(random.choice(PEG_COLORS))
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
        feedback = []
        code = list(codeToCopy)
        guess = list(guessToCopy)
        for i in range(0, CODE_LENGTH):
            if guess[i] == code[i]:
                code[i] = '-'
                guess[i] = ''
                feedback.append(RED)
        for i in range(0, CODE_LENGTH):
            if guess[i] in code:
               firstMatchedPos = self._findFirstMatchedColor(code, guess[i])
               code[firstMatchedPos] = '-'
               guess[i] = ''
               feedback.append(WHITE)
        winnerStatus = self._checkWinnerStatus(feedback)
        if winnerStatus == PLAYER_WON:
            print(WINNER_MSG)
            quit()
        else:
            return feedback


    def _findFirstMatchedColor(self, codeToCopy, guessItem):
        """ finds the position of the first matched color """
        code = list(codeToCopy)
        for i in range(0, CODE_LENGTH):
            if code[i] == guessItem:
                return i


    def _checkWinnerStatus(self, feedback):
        """ returns the winning code if player won """
        if feedback == WINNER_FEEDBACK:
            return PLAYER_WON
        else:
            print("Feedback: {}".format(feedback))


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
