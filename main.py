from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, CallbackContext
import telegram.ext.filters as Filters
import schedule
import time
import requests
import threading

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '7392929487:AAGh6NWUuDOd2YhLMrDvIMJ-iVZlrRs1I7o'
chat_id = 'feedcrowd_bot'  # Replace with your Telegram group chat ID
news_api_key = 'c954cab463f74b5d8f4def6707b9742e'  # Replace with your actual NewsAPI key

# Initialize the bot
bot = Bot(bot_token)

def fetch_web3_news():
    # Fetch Web3 news from an API (example: NewsAPI)
    response = requests.get(f'https://newsapi.org/v2/everything?q=web3&apiKey={news_api_key}')
    news = response.json()
    top_article = news['articles'][0]
    title = top_article['title']
    url = top_article['url']
    return f"{title}\n{url}"

def daily_news_roundup():
    news_summary = fetch_web3_news()
    bot.send_message(chat_id=chat_id, text=f"Daily Web3 News Roundup:\n{news_summary}")

# Schedule the daily task
schedule.every().day.at("09:00").do(daily_news_roundup)

# Function to run the schedule in a separate thread
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_schedule)
scheduler_thread.start()

# Initialize the updater
updater = Updater(bot_token)
dispatcher = updater.dispatcher

# Add a simple message handler (for demonstration purposes)
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling()
updater.idle()
