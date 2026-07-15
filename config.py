
import os
from dotenv import load_dotenv

load_dotenv()

BSC_RPC_URL = os.getenv("BSC_RPC_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

MIN_LIQUIDITY_USD = float(os.getenv("MIN_LIQUIDITY_USD", 5000))
DROP_ALERT_PERCENT = float(os.getenv("DROP_ALERT_PERCENT", 80))
