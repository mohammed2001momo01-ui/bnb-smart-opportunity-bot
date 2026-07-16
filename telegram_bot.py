
import telebot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def send_alert(opportunity):
    message = f"""
🚨 فرصة جديدة على BNB

💰 العملة: {opportunity['token']}
💲 السعر: {opportunity['price']} USD
📉 الهبوط: {opportunity['drop']}%
💧 السيولة: ${opportunity['liquidity']:,.2f}
📊 حجم التداول: ${opportunity['volume']:,.2f}

🔗 {opportunity['url']}
"""

    bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=message,
        disable_web_page_preview=True
    )
