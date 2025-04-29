from telegram import Bot

# Configuration
BOT_TOKEN = "7840777708:AAFhGEdTjsWBI5SU1D3lljBhNwurhAL3jqs"
CHAT_ID = "-1002593799966"

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Sets to track downloaded items
downloaded_items_yts = set()
downloaded_items_tg = set()
downloaded_items_club=set()
