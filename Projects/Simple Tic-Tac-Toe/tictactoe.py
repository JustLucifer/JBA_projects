def output_grid():
    print('-' * 9)
    print('|', *cells[:3], '|')
    print('|', *cells[3:6], '|')
    print('|', *cells[6:], '|')
    print('-' * 9)


def create_grid():
    return [' ' for x in range(9)]


def read_user_move():
    while True:
        try:
            move = input().split()
            x = int(move[0])
            y = int(move[1])
            if not 4 > x > 0 or not 4 > y > 0:
                raise Exception
        except ValueError:
            print('You should enter numbers!')
        except Exception:
            print('Coordinates should be from 1 to 3!')
        else:
            if update_grid(x, y):
                break


def update_grid(x, y):
    global status
    index = (((x - 1) * 3) + (y + 2)) - 3
    if cells[index] == ' ':
        if status == 0:
            cells[index] = 'X'
            status = 1
        elif status == 1:
            cells[index] = 'O'
            status = 0
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


def check_for_winner(*row):
    winner = ''
    for lst in row:
        for el in lst:
            if set(el) == {'X'}:
                winner = 'X'
            elif set(el) == {'O'}:
                winner = 'O'
    return winner


def analyze_grid():
    horizontal = [cells[:3], cells[3:6], cells[6:]]
    vertical = [cells[:7:3], cells[1::3], cells[2::3]]
    diagonal = [cells[::4], cells[2:8:2]]
    count_spaces = cells.count(' ')
    winner = check_for_winner(horizontal, vertical, diagonal)

    if winner != '':
        output_grid()
        if winner == 'X':
            print('X wins')
        elif winner == 'O':
            print('O wins')
        return True
    elif count_spaces == 0:
        output_grid()
        print('Draw')
        return True
    return False


def main():
    global cells
    global status
    cells = create_grid()
    status = 0
    while True:
        output_grid()
        read_user_move()
        if analyze_grid():
            break


if __name__ == '__main__':
    main()
