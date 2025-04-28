from telegram import Bot

# Configuration
BOT_TOKEN = "7557899973:AAHv97LXed5Ja7Hiy_hC-QNHPOzx-4okh9g"
CHAT_ID = "-1002681666316"

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Sets to track downloaded items
downloaded_items_yts = set()
downloaded_items_tg = set()
