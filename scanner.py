
import requests
from config import MIN_LIQUIDITY_USD, DROP_ALERT_PERCENT

DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/pairs/bsc"


def get_pairs():
    try:
        response = requests.get(DEXSCREENER_API, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data.get("pairs", [])
    except Exception as e:
        print(f"Scanner Error: {e}")
        return []


def find_opportunities():
    opportunities = []

    for pair in get_pairs():
        try:
            liquidity = float(pair.get("liquidity", {}).get("usd", 0))
            price_change = float(pair.get("priceChange", {}).get("h24", 0))
            volume = float(pair.get("volume", {}).get("h24", 0))

            if (
                liquidity >= MIN_LIQUIDITY_USD
                and price_change <= -DROP_ALERT_PERCENT
                and volume > 0
            ):
                opportunities.append({
                    "token": pair["baseToken"]["symbol"],
                    "price": pair["priceUsd"],
                    "drop": price_change,
                    "liquidity": liquidity,
                    "volume": volume,
                    "url": pair["url"]
                })

        except Exception:
            continue

    return opportunities
