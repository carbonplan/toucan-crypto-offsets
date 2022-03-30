import json
from pathlib import Path

import requests

endpoints = {
    'BCT': 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical'
    '?id=12949&convertId=2781&timeStart=1577932421&timeEnd=1648604021',
    'KLIMA': 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical'
    '?id=12873&convertId=2781&timeStart=1577932421&timeEnd=1648594800',
}


def get_coinmarket_data(url):
    r = requests.get(url)
    return r.json()


def get_closing_ts(data):
    return {quote['timeClose'][:10]: quote['quote']['close'] for quote in data['data']['quotes']}


def main():
    store = {}
    for coin, url in endpoints.items():
        data = get_coinmarket_data(url)
        ts = get_closing_ts(data)
        store[coin] = ts

    with open(Path(__file__).parents[1] / 'data/coin_price_ts.json', 'w') as f:
        json.dump(store, f)


if __name__ == '__main__':
    main()
