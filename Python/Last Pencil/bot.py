from random import randint
from errors import errors


def bot_make_move(turn, num):
    print(turn + "'s turn:")
    while True:
        try:
            if num == 1:
                num_of_pencils = 1
            elif num % 4 == 0:
                num_of_pencils = 3
            elif num % 4 == 3:
                num_of_pencils = 2
            elif num % 4 == 2:
                num_of_pencils = 1
            else:
                num_of_pencils = randint(1, 3)
            print(num_of_pencils)
            if num_of_pencils <= 0 or num_of_pencils > 3:
                raise ValueError
        except ValueError:
            print(errors[3])
        else:
            return num_of_pencils
