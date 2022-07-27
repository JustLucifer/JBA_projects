from coffee import Espresso, Latte, Cappuccino
import sys


class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.espresso = Espresso(250, 16, 4, 1)
        self.latte = Latte(350, 20, 7, 1, 75)
        self.cappuccino = Cappuccino(200, 12, 6, 1, 100)

    def show(self):
        print(f"The coffee machine has:\n"
              f"{self.water} ml of water\n"
              f"{self.milk} ml of milk\n"
              f"{self.beans} g of coffee beans\n"
              f"{self.cups} disposable cups\n"
              f"${self.money} of money\n")

    def buy_coffee(self):
        print('What do you want to buy?'
              ' 1 - espresso, 2 - latte, 3 - cappuccino,'
              ' back - to main menu:')
        coffee = input()
        if coffee != 'back':
            self.make_coffee(coffee=coffee)

    def make_coffee(self, coffee):
        if coffee == '1':
            coffee = self.espresso
        elif coffee == '2':
            coffee = self.latte
        else:
            coffee = self.cappuccino
        self.calc_amount(coffee=coffee)

    def calc_amount(self, coffee):
        if self.water < coffee.water:
            print(f"Not enough amount of water!")
        elif self.beans < coffee.beans:
            print(f"Not enough amount of beans!")
        elif self.milk < coffee.milk:
            print(f"Not enough amount of milk!")
        elif self.cups < coffee.cups:
            print(f"Not enough amount of cups!")
        else:
            print('I have enough resources, making you a coffee!\n')
            self.water -= coffee.water
            self.beans -= coffee.beans
            self.milk -= coffee.milk
            self.cups -= coffee.cups
            self.money += coffee.money

    def fill_coffee_machine(self):
        water = int(input('Write how many ml of water you want to add:\n'))
        milk = int(input('Write how many ml of milk you want to add:\n'))
        beans = int(input('Write how many grams of coffee beans you want to add:\n'))
        cups = int(input('Write how many disposable cups you want to add:\n'))
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money

    def menu(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()
            if action == 'buy':
                self.buy_coffee()
            elif action == 'fill':
                self.fill_coffee_machine()
            elif action == 'remaining':
                self.show()
            elif action == 'take':
                self.take_money()
            elif action == 'exit':
                sys.exit()

    def start(self):
        self.menu()
        print()
