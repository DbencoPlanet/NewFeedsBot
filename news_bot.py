import logging
import requests
import schedule
import time
import os
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
CHAT_ID = os.getenv('CHAT_ID')

# TELEGRAM_BOT_TOKEN = '7392929487:AAGh6NWUuDOd2YhLMrDvIMJ-iVZlrRs1I7o'
# NEWS_API_KEY = 'c954cab463f74b5d8f4def6707b9742e'  # Replace with your News API key
# CHAT_ID = '7153428305'

NEWS_API_URL = 'https://newsapi.org/v2/everything'
NEWS_QUERY = 'web3'  # Query parameter for the news topic

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I will send you news updates at scheduled times.')

def fetch_news() -> str:
    """Fetch top news headlines from News API."""
    response = requests.get(f'{NEWS_API_URL}?q={NEWS_QUERY}&apiKey={NEWS_API_KEY}')
    news_data = response.json()
    articles = news_data.get('articles', [])

    if not articles:
        return "No news available at the moment."

    news_list = [f"{article['title']} - {article['source']['name']}" for article in articles[:5]]
    return '\n'.join(news_list)

async def send_news(bot: Bot, chat_id: str) -> None:
    """Send news to the specified chat."""
    news = fetch_news()
    await bot.send_message(chat_id=chat_id, text=news)

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()
    logger.info("Bot started polling...")

    # Schedule news feed
    # chat_id = 123456789  # Replace with your actual chat ID
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    schedule.every().day.at("08:00").do(lambda: send_news(bot, CHAT_ID))
    schedule.every().day.at("20:00").do(lambda: send_news(bot, CHAT_ID))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
    # main()





# import logging
# import requests
# import schedule
# import time
# import os
# from telegram import Update, Bot
# from telegram.ext import Application, CommandHandler, ContextTypes
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# # NEWS_API_KEY = os.getenv('NEWS_API_KEY')
# # CHAT_ID = os.getenv('CHAT_ID')

# TELEGRAM_BOT_TOKEN = '7392929487:AAGh6NWUuDOd2YhLMrDvIMJ-iVZlrRs1I7o'
# NEWS_API_KEY = 'c954cab463f74b5d8f4def6707b9742e'  # Replace with your News API key
# CHAT_ID = '7153428305'

# NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
# NEWS_COUNTRY = 'us'


# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text('Hi! I will send you news updates at scheduled times.')

# def fetch_news() -> str:
#     params = {
#         'apiKey': NEWS_API_KEY,
#         'country': NEWS_COUNTRY,
#     }
#     response = requests.get(NEWS_API_URL, params=params)
#     news_data = response.json()
#     articles = news_data.get('articles', [])
#     if not articles:
#         return "No news available at the moment."
#     news_list = [f"{article['title']} - {article['source']['name']}" for article in articles[:5]]
#     return '\n'.join(news_list)

# async def send_news(bot: Bot, chat_id: str) -> None:
#     news = fetch_news()
#     await bot.send_message(chat_id=chat_id, text=news)

# def main() -> None:
#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
#     application.add_handler(CommandHandler("start", start))
#     application.run_polling()

#     # chat_id = 123456789  # Replace with your actual chat ID
#     bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
#     schedule.every().day.at("08:00").do(lambda: send_news(bot, CHAT_ID))
#     schedule.every().day.at("20:00").do(lambda: send_news(bot, CHAT_ID))

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == '__main__':
#     main()












# import logging
# import requests
# import schedule
# import time
# from telegram import Update, Bot
# from telegram.ext import Application, CommandHandler, ContextTypes

# # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
# TELEGRAM_BOT_TOKEN = '7392929487:AAGh6NWUuDOd2YhLMrDvIMJ-iVZlrRs1I7o'
# NEWS_API_KEY = 'c954cab463f74b5d8f4def6707b9742e'  # Replace with your News API key
# NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
# NEWS_COUNTRY = 'us'  # Replace with your desired country code (e.g., 'us', 'gb')

# # Set up logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     await update.message.reply_text('Hi! I will send you news updates at scheduled times.')

# def fetch_news() -> str:
#     """Fetch top news headlines from News API."""
#     params = {
#         'apiKey': NEWS_API_KEY,
#         'country': NEWS_COUNTRY,
#     }
#     response = requests.get(NEWS_API_URL, params=params)
#     news_data = response.json()
#     articles = news_data.get('articles', [])

#     if not articles:
#         return "No news available at the moment."

#     news_list = [f"{article['title']} - {article['source']['name']}" for article in articles[:5]]
#     return '\n'.join(news_list)

# async def send_news(bot: Bot, chat_id: str) -> None:
#     """Send news to the specified chat."""
#     news = fetch_news()
#     await bot.send_message(chat_id=chat_id, text=news)

# def main() -> None:
#     """Start the bot."""
#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

#     # Register command handlers
#     application.add_handler(CommandHandler("start", start))

#     # Start the Bot
#     application.run_polling()
#     logger.info("Bot started polling...")

#     # Schedule news feed
#     chat_id = '7153428305'  # Replace with your Telegram chat ID
#     bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
#     schedule.every().day.at("08:00").do(lambda: send_news(bot, chat_id))
#     schedule.every().day.at("20:00").do(lambda: send_news(bot, chat_id))

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == '__main__':
#     main()
