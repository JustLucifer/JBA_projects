from calculations import calculation
from random import randint, choice
import sys


class App:

    def __init__(self):
        self.opers = '*-+'
        self.score = 0
        self.level_description = {1: '1 - simple operations with numbers 2-9',
                                  2: '2 - integral squares of 11-29'}

    def create_math_task(self):
        opers = '+-*'
        if self.level == 1:
            self.x, self.y = randint(2, 9), randint(2, 9)
            self.oper = choice(opers)
        else:
            self.x = randint(11, 29)

    def calculate_math_task_result(self):
        if self.level == 1:
            self.res = calculation(self.x, self.oper, self.y)
        else:
            self.res = self.x ** 2

    def output_math_task(self):
        if self.level == 1:
            print(self.x, self.oper, self.y)
            self.user_answer = self.read_user_answer()
        else:
            print(self.x)
            self.user_answer = self.read_user_answer()

    def read_user_answer(self):
        while True:
            try:
                answer = int(input())
            except ValueError:
                print('Wrong format! Try again.')
            else:
                return answer

    def check_user_answer(self):
        if self.res == self.user_answer:
            print('Right!')
            self.score += 1
        else:
            print('Wrong!')

    def choose_level_difficulty(self):
        msg = "Which level do you want? Enter a number:\n" \
              "1 - simple operations with numbers 2-9\n" \
              "2 - integral squares of 11-29\n"
        while True:
            try:
                level = int(input(msg))
                assert 0 < level < 3
            except (ValueError, AssertionError):
                print('Incorrect format.')
            else:
                return level

    def save_score_to_file(self):
        lst_yeses = ('yes', 'YES', 'y', 'Yes')
        print(f'Your mark is {self.score}/5. Would you like to save the result?'
              ' Enter yes or no.')
        if input() in lst_yeses:
            name = input('What is your name?\n')
            with open('results.txt', 'a') as f:
                print("{}: {}/5 in level {} ({})."
                      .format(name,
                              self.score,
                              self.level,
                              self.level_description[self.level]),
                      file=f)
            print('The results are saved in "results.txt".')
        else:
            sys.exit()

    def run(self):
        self.level = self.choose_level_difficulty()
        for _ in range(5):
            self.create_math_task()
            self.calculate_math_task_result()
            self.output_math_task()
            self.check_user_answer()
        self.save_score_to_file()
