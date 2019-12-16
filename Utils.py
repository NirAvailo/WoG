import os

SCORES_FILE_NAME = 'Scores.txt'
ERROR_MESSAGE = 'Something went wrong..'


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
