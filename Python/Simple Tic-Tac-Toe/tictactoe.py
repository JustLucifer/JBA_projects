def output_grid():
    print('-' * 9)
    print('|', *cells[:3], '|')
    print('|', *cells[3:6], '|')
    print('|', *cells[6:], '|')
    print('-' * 9)


def create_grid():
    return [' ' for _ in range(9)]


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


def analyze_grid():
    combinations = [cells[:3], cells[3:6], cells[6:],  # horizontal
                    cells[:7:3], cells[1::3], cells[2::3],  # vertical
                    cells[::4], cells[2:8:2]]  # diagonal

    for el in combinations:
        if set(el) == {'X'}:
            print('X wins')
            return True
        elif set(el) == {'O'}:
            print('O wins')
            return True
    
    if cells.count(' ') == 0:
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
