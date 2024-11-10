import json

from supabase.client import Client, create_client
from config import SB_URL, SB_KEY

supabase: Client = create_client(SB_URL, SB_KEY)


def export_prices(filename: str, table: str):
    values = []
    with open(filename, "r") as file:
        prices = json.loads(file.read())
        for item in prices:
            name = item.get("market_hash_name")
            name = name.replace("\u2605 ", "")
            name = name.replace("\u2122", "")

            steam = None
            buff = None
            skinport = item.get("suggested_price", None)
            values.append({"name": name, "steam": steam, "skinport": skinport, "buff": buff})
        # print(values)
        supabase.table(table).upsert(values, on_conflict="name").execute()
        print(f"Exporting prices from {filename} to table {table}")


def update_prices():
    res = supabase.rpc("update_item_prices", params={}).execute()
    # print(res)
