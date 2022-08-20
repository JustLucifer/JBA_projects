from random import choice


class BillSplitter:

    def __init__(self):
        self.friends = {}

    def get_friends_number(self):
        print('Enter the number of friends joining (including you):')
        return int(input())

    def get_friends(self):
        num = self.get_friends_number()
        if num <= 0:
            print('\nNo one is joining for the party')
        else:
            print('Enter the name of every friend (including you),'
                  ' each on a new line:')
            self.friends = {input(): 0 for key in range(num)}
            print()
            return True

    def take_final_bill(self):
        print('Enter the total bill value:')
        return float(input())

    def split_bill(self):
        bill = self.take_final_bill()
        lucky_feature = input('\nDo you want to use the "Who is lucky?" '
                              'feature? Write Yes/No:\n')
        if lucky_feature == 'Yes':
            self.choose_lucky_one()
            return round(bill / (len(self.friends) - 1), 2)
        else:
            self.lucky_one = ''
            print('No one is going to be lucky')
        return round(bill / len(self.friends), 2)

    def choose_lucky_one(self):
        self.lucky_one = choice(list(self.friends))
        print(f'{self.lucky_one} is the lucky one!')

    def update_dict_with_sum(self, total):
        for friend in self.friends:
            if friend == self.lucky_one:
                self.friends[friend] = 0
            else:
                self.friends[friend] = total

    def output_friends_dict(self):
        print()
        print(self.friends)

    def start(self):
        if self.get_friends():
            total = self.split_bill()
            self.update_dict_with_sum(total=total)
            self.output_friends_dict()
