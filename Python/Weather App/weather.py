import requests as r
import datetime
from api import BASE_URL, API_KEY


def get_weather(city):
    request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
    response = r.get(request_url)
    
    if response.status_code == 200:
        data = response.json()
        state = data.get('weather')[0]['description'].capitalize()
        temp = round(data.get('main')['temp'] - 273.15, 2)
        local_time = get_proper_time(data=data)
        card = get_card_by_time(int(local_time))
        return {'degrees': temp, 'card': card, 'state': state}
    else:
        print('Error occurred')


def get_proper_time(data):
    tz=datetime.timezone(datetime.timedelta(seconds=int(data['timezone'])))
    t = datetime.datetime.now(tz=tz).time()
    return '{}:{}'.format(t.hour, t.minute).split(':')[0]


def get_card_by_time(hours):
    cards = ('night', 'day', 'evening-morning')
    if 0 <= hours <= 5:
        card = cards[0]
    elif 5 < hours < 17:
        card = cards[1]
    else:
        card = cards[2]
    return card
