from random import shuffle, choice, randint


def create_domino_set():
    full_domino_set = []
    for i in range(7):
        for j in range(i, 7):
            full_domino_set.append([i, j])
    return full_domino_set


def shuffle_dominoes(dominoes):
    shuffle(dominoes)
    return dominoes


def split_dominoes(dominoes):
    while True:
        dominoes = shuffle_dominoes(dominoes=dominoes)
        stock = dominoes[:14]
        computer_pieces = dominoes[14:21]
        player_pieces = dominoes[21:]
        snake, status = define_first_domino(computer_pieces, player_pieces)
        if snake:
            break
    return {'stock': stock,
            'pc_pieces': computer_pieces,
            'pl_pieces': player_pieces,
            'snake': [snake],
            'status': status,
            }


def define_first_domino(computer, player):
    doubled = []
    lst = computer + player
    for i in lst:
        if i[0] == i[1]:
            doubled.append(i)
    first_domino = max(doubled)

    if first_domino in computer:
        computer.remove(first_domino)
        status = 'player'
    elif first_domino in player:
        player.remove(first_domino)
        status = 'computer'
    else:
        return False
    return first_domino, status


def check_for_draw():
    count = 0
    for i in range(7):
        for j in data['snake']:
            if i == j[0] or i == j[1]:
                count += 1
        if count == 7:
            return True
        return False


def determine_winner():
    if len(data['pc_pieces']) == 0:
        data['status'] = 'Status: The game is over. The computer won!'
    elif len(data['pl_pieces']) == 0:
        data['status'] = 'Status: The game is over. You won!'
    elif check_for_draw():
        data['status'] = "Status: The game is over. It's a draw!"


def output_grid():
    print('=' * 70)
    print(f'Stock pieces: {len(data["stock"])}')
    print(f'Computer pieces: {len(data["pc_pieces"])}\n')
    if len(data["snake"]) < 7:
        print(*data["snake"])
    else:
        print(*data["snake"][:3], '...', *data["snake"][-3:], sep='')
    print(f'\nYour pieces:')
    for n, i in enumerate(data['pl_pieces']):
        print(f'{n + 1}:{i}')
    print()
    determine_winner()
    if data['status'] == 'player':
        print("Status: It's your turn to make a move. Enter your command.")
    elif data['status'] == 'computer':
        print("Status: Computer is about to make a move. "
              "Press Enter to continue...")
    else:
        print(data['status'])
        return True


def validate_player_move(move):
    if move == 0:
        piece = data['stock'].pop(randint(0, len(data['stock']) - 1))
        data['pl_pieces'].append(piece)
        data['status'] = 'computer'
        return True
    elif move > 0:
        piece = data['pl_pieces'][move - 1]
        if piece[0] == data['snake'][-1][1]:
            data['snake'].append(data['pl_pieces'].pop(move - 1))
            data['status'] = 'computer'
            return True
        elif piece[1] == data['snake'][-1][1]:
            piece.reverse()
            data['snake'].append(data['pl_pieces'].pop(move - 1))
            data['status'] = 'computer'
            return True
    elif move < 0:
        piece = data['pl_pieces'][abs(move) - 1]
        if piece[0] == data['snake'][0][0]:
            piece.reverse()
            data['snake'].insert(0, data['pl_pieces'].pop(abs(move) - 1))
            data['status'] = 'computer'
            return True
        elif piece[1] == data['snake'][0][0]:
            data['snake'].insert(0, data['pl_pieces'].pop(abs(move) - 1))
            data['status'] = 'computer'
            return True
    else:
        return False


def player_move(length):
    while True:
        try:
            move = int(input())
            if abs(move) > length:
                raise ValueError
        except ValueError:
            print('Invalid input. Please try again.')
        else:
            if validate_player_move(move=move):
                break
            else:
                print('Illegal move. Please try again.')


def validate_computer_move(move):
    if move[0] == data['snake'][-1][1]:
        data['snake'].append(move)
        return True
    elif move[1] == data['snake'][-1][1]:
        move.reverse()
        data['snake'].append(move)
        return True
    elif move[0] == data['snake'][0][0]:
        move.reverse()
        data['snake'].insert(0, move)
        return True
    elif move[1] == data['snake'][0][0]:
        data['snake'].insert(0, move)
        return True
    else:
        return False


def calculate_move():
    d = dict.fromkeys([0, 1, 2, 3, 4, 5, 6], 0)
    temp_dict = {}
    for i in data['pc_pieces']:
        d[i[0]] += 1
        d[i[1]] += 1

    for j in data['pc_pieces']:
        res = d[j[0]] + d[j[1]]
        temp_dict[res] = j
    return temp_dict


def computer_move():
    input()
    temp_dict = calculate_move()
    while True:
        try:
            move = temp_dict[max(temp_dict)]
        except ValueError:
            move = data['stock'].pop(randint(0, len(data['stock']) - 1))
            data['pc_pieces'].append(move)
            break
        else:
            if validate_computer_move(move=move):
                data['pc_pieces'].remove(move)
                break
            else:
                del temp_dict[max(temp_dict)]
    data['status'] = 'player'


def gameplay():
    while True:
        if output_grid():
            break
        if data['status'] == 'player':
            player_move(len(data['pl_pieces']))
        else:
            computer_move()


def main():
    global data
    domino_set = create_domino_set()
    data = split_dominoes(domino_set)
    gameplay()


if __name__ == '__main__':
    main()
