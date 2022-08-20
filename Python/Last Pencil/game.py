from errors import errors
from bot import bot_make_move

players = ('John', 'Jack')


def pencil_number():
    print('How many pencils would you like to use:')
    while True:
        try:
            num = int(input())
            if num < 0:
                raise ValueError
        except ValueError:
            print(errors[0])
        else:
            if num == 0:
                print(errors[1])
                continue
            return num


def first_player():
    print('Who will be the first ({}, {} ):'.format(players[0], players[1]))
    while True:
        name = input()
        if name not in players:
            print(errors[2].format(players[0], players[1]))
            continue
        return name


def output():
    print('|' * pencils)


def determine_first_turn(f_player):
    first = f_player
    if f_player == players[0]:
        second = players[1]
    else:
        second = players[0]
    return first, second


def make_move(turn):
    global pencils
    if turn == 'Jack':
        num_of_pencils = bot_make_move(turn, pencils)
        return num_of_pencils
    print(turn + "'s turn:")
    while True:
        try:
            num_of_pencils = int(input())
            if num_of_pencils <= 0 or num_of_pencils > 3:
                raise ValueError
        except ValueError:
            print(errors[3])
        else:
            return num_of_pencils


def choose_turn(turn, first, second):
    if turn == first:
        turn = second
    else:
        turn = first
    return turn


def gameplay(f_player):
    global pencils
    first, second = determine_first_turn(f_player=f_player)
    turn = first
    while pencils > 0:
        output()
        delete_pencils = make_move(turn=turn)
        if delete_pencils > pencils:
            print(errors[4])
            continue
        pencils -= delete_pencils
        turn = choose_turn(turn=turn,
                           first=first,
                           second=second)
    print(f'{turn} won!')


def main():
    global pencils
    pencils = pencil_number()
    f_player = first_player()
    gameplay(f_player=f_player)


if __name__ == '__main__':
    main()
