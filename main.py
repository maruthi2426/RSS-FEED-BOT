from flask import Flask, jsonify
import asyncio
import threading
import schedule
import time
from yts_rss import fetch_and_post_yts_feeds
from torrentgalaxy_rss import fetch_and_post_torrentgalaxy_feeds

# Flask app
app = Flask(__name__)
PORT = 3000

@app.route('/', methods=['GET'])
def home():
    """Home route"""
    return jsonify({"message": "Welcome to the YT RSS Bot API!"})

@app.route('/yts', methods=['GET'])
def handle_yts_feed():
    """Fetch and post YTS RSS feed"""
    asyncio.run(fetch_and_post_yts_feeds())
    return jsonify({"message": "YTS feeds fetched and posted!"})

@app.route('/torrentgalaxy', methods=['GET'])
def handle_torrentgalaxy_feed():
    """Fetch and post TorrentGalaxy RSS feed"""
    asyncio.run(fetch_and_post_torrentgalaxy_feeds())
    return jsonify({"message": "TorrentGalaxy feeds fetched and posted!"})

# Background task for scheduled feeds
def schedule_task():
    schedule.every(1).minutes.do(lambda: asyncio.run(fetch_and_post_yts_feeds()))
    schedule.every(1).minutes.do(lambda: asyncio.run(fetch_and_post_torrentgalaxy_feeds()))
    while True:
        schedule.run_pending()
        time.sleep(1)

# 🔥 Always start the scheduler thread when the app is imported or run
threading.Thread(target=schedule_task, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
