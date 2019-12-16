import time
import random
from Utils import screen_cleaner


def generate_sequence(difficulty):
    # generate a new list of random numbers
    numbers = []
    show = ''
    while len(numbers) < difficulty:
        n = random.randint(1, 101)
        numbers.append(n)
        # build display text
        if len(show) > 0:
            show += ' '
        show += str(n)
    # show cards
    print(show)
    # hide cards
    time.sleep(0.7)
    screen_cleaner()
    return numbers


def get_list_from_user(difficulty):
    # get a list of number from the user
    numbers = []
    print('After seeing the numbers enter the numbers you saw, each one separated with Enter.')
    while len(numbers) < difficulty:
        try:
            n = int(input())
        except ValueError:
            # invalid input format, the user need to try again
            continue
        if n > 0:
            numbers.append(n)
    return numbers


def is_list_equal(list_a, list_b):
    # compare two list of numbers, there length must be the same and without any differences.
    return not (len(list_a) != len(list_b) or len(set(list_a).difference(list_b)) > 0)


def play(difficulty):
    # play the memory game
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    won = is_list_equal(list_a, list_b)
    if won:
        print('You have a good memory')
    else:
        print('You gave wrong numbers')
    return won


