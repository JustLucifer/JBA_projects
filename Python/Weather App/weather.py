from random import randint, choice


def get_weather():
    cards = ('night', 'day', 'evening-morning')
    degrees = randint(-15, 35)
    card = choice(cards)
    if degrees < 5:
        state = 'Cold'
    elif degrees < 15:
        state = 'Chilly'
    else:
        state = 'Sunny'
    return {'degrees': degrees, 'card': card, 'state': state}
