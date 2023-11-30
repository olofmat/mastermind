#!/usr/bin/python3
""" Game execution """
from codeBreaker import CodeBreaker
from codeMaker import CodeMaker
from constants import *
from os import system, name
import random


def clear():
    """clears the console"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def isGameAgainstBot(botOrNot):
    """ checks if user wants to play with bot """
    if botOrNot in ['Y', 'y', 'yes', 'Yes', 'YES']:
        return True
    elif botOrNot in ['N', 'n', 'no', 'No', 'NO']:
        return False
    else:
        print("I did not recognize your answer. Goodbye...")
        quit()

def main():
    """ point of execution """
    print(WELCOME_MESSAGE, '\n')
    botOrNot = input(BOT_OR_TWO_PLAYER_PROMPT)
    gameIsAgainstBot = isGameAgainstBot(botOrNot)
    codeMaker = CodeMaker()
    codeBreaker = CodeBreaker()
    if gameIsAgainstBot:
        code = codeMaker.createRandomCode()
    else:
        code = codeMaker.createCode()
        clear()

    print()
    print(GUESS_FORMATTING_INSTRUCTIONS)
    guessCount = 0
    while guessCount <= MAX_NUMBER_OF_GUESSES:
        if guessCount == MAX_NUMBER_OF_GUESSES:
            print(GUESSES_MAXED_OUT_MESSAGE)
            quit()
        else:
            guess = codeBreaker.makeGuess(guessCount)
            codeMaker.provideFeedback(code, guess)
            guessCount += 1


if __name__ == '__main__':
    main()
