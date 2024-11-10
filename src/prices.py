import json
import requests

URL = "https://api.skinport.com/v1/items?app_id=730"


def get_prices():
    res = requests.get(URL)

    prices = json.loads(res.content)

    print("Fetched prices for {} items.".format(len(prices)))

    with open("../prices.json", "w") as file:
        file.write(json.dumps(prices))
