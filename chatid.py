import logging
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TELEGRAM_BOT_TOKEN = '7392929487:AAGh6NWUuDOd2YhLMrDvIMJ-iVZlrRs1I7o'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f'Your chat ID is: {chat_id}')
    logger.info(f'Chat ID: {chat_id}')

def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
