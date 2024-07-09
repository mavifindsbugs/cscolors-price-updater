from time import sleep
import schedule
from datetime import datetime
from zoneinfo import ZoneInfo

from config import SCAN_TIME, TIMEZONE

from prices import get_prices
from exporter import export_prices, update_prices


def update():
    now = datetime.now(ZoneInfo(TIMEZONE))
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Starting update at {formatted_now}\n")

    get_prices()
    export_prices("../prices.json", "Prices")
    update_prices()

    now = datetime.now(ZoneInfo(TIMEZONE))
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")
    next_run = schedule.next_run().astimezone(ZoneInfo(TIMEZONE))
    formatted_next_run = next_run.strftime("%d/%m/%Y %H:%M:%S")

    time_difference = next_run - now
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"Update finished at {formatted_now}, next update at {formatted_next_run} in "
        f"{time_difference.days}d {hours}h {minutes}m {seconds}s\n"
    )


def schedule_updates():
    print("Starting scheduler ...")
    schedule.every().day.at(SCAN_TIME).do(update)
    schedule.run_all()
    while True:
        schedule.run_pending()
        sleep(5)
