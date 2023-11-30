# colors of code pegs
BLUE = 'blue'
PURPLE = 'purple'
YELLOW = 'yellow'
ORANGE = 'orange'
GREEN = 'green'
BLACK = 'black'

# colors of feedback pegs
RED = 'red'
WHITE = 'white'

# list of peg colors random will choose from
PEG_COLORS = [BLUE, PURPLE, YELLOW, ORANGE, GREEN, BLACK]

# list of feedback needed to win the game
WINNER_FEEDBACK = [RED, RED, RED, RED]

# number of turns or guesses
MAX_NUMBER_OF_GUESSES = 10

# length of the code and a guess
GUESS_LENGTH = 4
CODE_LENGTH = 4

# status codes for validation
UNKNOWN_COLOR_ERROR_CODE = 'UNKNOWN_COLOR_ERROR_CODE'
MISSING_INPUT_ERROR_CODE = 'MISSING_INPUT_ERROR_CODE'

# win or lose status codes
PLAYER_WON = 'PLAYER_WON'

# winning message
WINNER_MSG = 'You won! Congrats Mastermind!'

# user input error message
USER_INPUT_ERROR_MSG = 'Please check your answer and try again'

# prompt for user to start guessing and brief instructions before round begins
GUESS_FORMATTING_INSTRUCTIONS = 'Each guess has to be 4 colors separated by' \
' a space.\nThe colors you may use for guessing are as follows:\nblue,' \
' purple, yellow, orange, green and black.\nYou get 10 guesses to crack' \
' the code. Good luck!\n'
GUESS_PROMPT = 'Enter your guess: '

# prompt for Player 2 to enter code
CODE_PROMPT = 'Enter 4 colors separated by a space: '

# welcome message
WELCOME_MESSAGE = 'Welcome to Mastermind!'

# prompt for bot or 2 player
BOT_OR_TWO_PLAYER_PROMPT = 'Would you like to play against a bot? Y/N? '

# message for guesses maxed out
GUESSES_MAXED_OUT_MESSAGE = 'You have exhausted your guesses. Try again next' \
' time.'
