import requests


def get_currency_code():
    return input().upper()


def get_popular_currencies(code):
    cache_dict = {}
    r = requests.get(f'http://www.floatrates.com/daily/{code}.json').json()
    if code.upper() != 'USD' and code.upper() != 'EUR':
        cache_dict['USD'] = r['usd']['rate']
        cache_dict['EUR'] = r['eur']['rate']
    elif code.upper() == 'USD':
        cache_dict['EUR'] = r['eur']['rate']
    elif code.upper() == 'EUR':
        cache_dict['USD'] = r['usd']['rate']
    return cache_dict


def make_request(exchange):
    r = requests.get(f'http://www.floatrates.com/daily/{currency}.json').json()
    return r[exchange.lower()]['rate']


def get_exchange_for():
    return input().upper()


def get_amount_money():
    return float(input())


def calculate_result(rate, amount):
    return round(amount * rate, 2)


def check_cache(cache, exchange, amount):
    print('Checking the cache...')
    if exchange in cache:
        print('Oh! It is in the cache!')
        return calculate_result(cache[exchange], amount)

    print('Sorry, but it is not in the cache!')
    rate = make_request(exchange=exchange)
    cache[exchange] = rate
    return calculate_result(rate=rate, amount=amount)


def output_result(res, exchange):
    print('You received {} {}.'.format(res, exchange))


def main():
    global currency
    currency = get_currency_code()
    cache = get_popular_currencies(currency)

    while True:
        exchange = get_exchange_for()
        if exchange == '':
            break
        amount = get_amount_money()
        res = check_cache(cache=cache,
                          exchange=exchange,
                          amount=amount)
        output_result(res=res, exchange=exchange)


if __name__ == '__main__':
    main()

