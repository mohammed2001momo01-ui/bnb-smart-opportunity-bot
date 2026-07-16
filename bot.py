
import time

from scanner import find_opportunities
from telegram_bot import send_alert


def run():
    sent = set()

    while True:
        opportunities = find_opportunities()

        for opportunity in opportunities:
            token = opportunity["token"]

            if token not in sent:
                send_alert(opportunity)
                sent.add(token)

        time.sleep(60)


if __name__ == "__main__":
    run()
