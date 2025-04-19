import feedparser
import asyncio
from telegram.constants import ParseMode
from config import bot, CHAT_ID, downloaded_items_tg

async def fetch_and_post_torrentgalaxy_feeds():
    """Fetch Pornrips RSS feeds and post new items to Telegram"""
    try:
        # Fetch RSS feed
        feed = feedparser.parse("https://pornrips.to/feed/torrents")
        if not feed.entries:
            print("No entries found in the Pornrips RSS feed.")
            return

        # Process each feed entry
        for item in feed.entries:
            title = item.get("title", "No Title")
            link = item.get("link", "")
            torrent_file = None

            # Find torrent file link
            if "links" in item:
                for link_item in item.links:
                    href = link_item.get("href", "")
                    if href.endswith(".torrent"):
                        torrent_file = href

            # Skip if already posted
            if link not in downloaded_items_tg:
                # Construct message
                message = f"🎥 <b>{title}</b>\n\n"

                # Add Torrent File link if available               
                message += f"🔗 <b>Torrent File:</b> <a href='{link}'>Pornrips</a>\n\n"

                # Add Source as plain text in <code> format
                message += f"🧲 <b>Magnet Link:</b> <code>{link}</code>"

                # Send message to Telegram
                await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)
                downloaded_items_tg.add(link)
                await asyncio.sleep(1)

    except Exception as e:
        print(f"Error in Pornrips feed handling: {e}")
