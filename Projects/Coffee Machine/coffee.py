class Espresso:
    def __init__(self, water, beans, money, cups, milk=0):
        self.water = water
        self.beans = beans
        self.milk = milk
        self.cups = cups
        self.money = money


class Latte(Espresso):
    def __init__(self, water, beans, money, cups, milk=0):
        super().__init__(water, beans, money, cups, milk)


class Cappuccino(Espresso):
    def __init__(self, water, beans, money, cups, milk=0):
        super().__init__(water, beans, money, cups, milk)
