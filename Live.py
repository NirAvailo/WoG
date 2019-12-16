from Utils import ERROR_MESSAGE
from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from Score import add_score


def welcome(name):
    # show welcome message
    return 'Hello ' + name + \
           """ and welcome to the World of Games (WoG).
Here you can find many cool games to play.
"""


def load_game():
    # ask the user to enter a game
    print('Please choose a game to play: \n',
          '\t 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n',
          '\t 2. Guess Game - guess a number and see if you chose like the computer.')
    try:
        game = int(input())
    except ValueError:
        game = 0
    if game == 1:
        print('You have choose to play the Memory Game.')
    elif game == 2:
        print('You have choose to play the Guess Game.')
    # ask the user to enter the game difficulty
    try:
        difficulty = int(input('Please choose game difficulty from 1 to 5: \n'))
    except ValueError:
        difficulty = 0
    # play the game
    message = start_game(game, difficulty)
    if message is not None:
        print(message)


def start_game(game, difficulty):
    if (difficulty < 1 or difficulty > 5):
        # invalid difficulty input
        return ERROR_MESSAGE
    elif game == 1:
        # user want to play the memory game
        won = play_memory_game(difficulty)
    elif game == 2:
        # user want to play the guess game
        won = play_guess_game(difficulty)
    else:
        # invalid game input
        return ERROR_MESSAGE
    if won:
        # add winning score to the user in case he won the game
        add_score(difficulty)
    # NOTE:
    # according to diagram in the project specification it should call load_game function no mather what the
    # result.
    load_game()


