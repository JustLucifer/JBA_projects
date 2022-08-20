from random import choice
import sys


def greeting():
    print('H A N G M A N')


def choose_random_word():
    words = ('python', 'java', 'swift', 'javascript')
    return choice(words)


def create_hint(word):
    global hint
    hint = ['-' for _ in range(len(word))]


def output_hint():
    print('\n' + ''.join(hint))


def check_win():
    if hint.count('-') == 0:
        return True
    return False


def another_letter_check(word, letter):
    global lives

    if letter in repeted_letters:
        print("You've already guessed this letter.")
    else:
        if letter in word:
            for n, i in enumerate(word):
                if i == letter:
                    hint[n] = letter
                    repeted_letters.append(letter)
        else:
            print("That letter doesn't appear in the word.")
            repeted_letters.append(letter)
            lives -= 1


def guess_letter(word):
    word = list(word)
    output_hint()
    try:
        letter = input('Input a letter: ')
        assert len(letter) == 1
        if letter.isupper() or not letter.isalpha():
            raise ValueError
    except AssertionError:
        print('Please, input a single letter.')
    except ValueError:
        print('Please, enter a lowercase letter from the English alphabet.')
    else:
        another_letter_check(word=word, letter=letter)


def gameplay():
    global lives
    global repeted_letters
    global win_score
    global lose_score
    lives = 8
    repeted_letters = []
    hidden_word = choose_random_word()
    create_hint(hidden_word)

    while lives > 0:
        guess_letter(hidden_word)
        if check_win():
            output_hint()
            print(f'You guessed the word {hidden_word}!')
            print('You survived!')
            win_score += 1
            break
    else:
        print('You lost!')
        lose_score += 1


def menu():
    action = input('Type "play" to play the game, '
                   '"results" to show the scoreboard, and "exit" to quit: ')

    if action == 'play':
        gameplay()
    elif action == 'results':
        print(f'You won: {win_score} times.')
        print(f'You lost: {lose_score} times.')
    elif action == 'exit':
        sys.exit()


def main():
    global win_score
    global lose_score
    win_score = 0
    lose_score = 0

    greeting()
    while True:
        menu()


if __name__ == '__main__':
    main()
