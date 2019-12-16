import random


def generate_number(difficulty):
    # generate a new random number
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    # ask the user to enter his guessing number
    try:
        n = int(input('Guess a number between 1 and {0}: \n'.format(difficulty)))
        return n
    except ValueError:
        return 0


def compare_results(difficulty, secret_number):
    # ask the user to guess a number and compare it to given number
    guess = get_guess_from_user(difficulty)
    return guess == secret_number


def play(difficulty):
    # play the game
    secret_number = generate_number(difficulty)
    won = compare_results(difficulty, secret_number)
    if won:
        print('You have guessed the right number')
    else:
        print('Wrong, the right number is', secret_number)
    return won

