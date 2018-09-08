from random import randint, choice
from calc_function import calculate


def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 9)
    y = randint(0, 9)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    result = calculate(x, y, op) + error

    return [x, y, op, result]


def check_answer(x, y, op, result, user_choice):
    if result == calculate(x, y, op):
        if user_choice is True:
            return True
        else:
            return False

    else:
        if user_choice is True:
            return False
        else:
            return True
