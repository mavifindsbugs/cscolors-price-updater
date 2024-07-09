import json
import requests

URL = "https://prices.csgotrader.app/latest/prices_v6.json"


def get_prices():
    prices = {}
    res = requests.get(URL)

    for item, data in json.loads(res.content).items():
        item = item.replace("\u2605 ", "")
        item = item.replace("\u2122", "")
        prices[item] = data

    print("Fetched prices for {} items.".format(len(prices)))

    with open("../prices.json", "w") as file:
        file.write(json.dumps(prices))
