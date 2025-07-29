"""
Telegram bot command and message handlers.
"""
from telegram import ForceReply, Update
from telegram.ext import ContextTypes
import jmdict
import logging


logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    logger.info("Received /start command.")
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )
    logger.info("Sent /start command reply.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    logger.info("Received /help command.")
    await update.message.reply_text("Help!")
    logger.info("Sent /help command reply.")


async def random_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random JMDict entry to the user."""
    logger.info("Received /random command.")
    entry = jmdict.get_random_jmdict_entry()
    entry = jmdict.format_jmdict_entry(entry)
    await update.message.reply_text(entry)
    logger.info("Sent /random command reply.")


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add the chat to daily notifications."""
    logger.info("Received /subscribe command.")
    chat_id = update.effective_chat.id

    if 'chats' not in context.bot_data:
        context.bot_data['chats'] = set()

    context.bot_data['chats'].add(chat_id)
    await update.message.reply_text("You've been subscribed to daily random entries!")
    logger.info("Sent /subscribe command reply.")


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove the chat from daily notifications."""
    logger.info("Received /unsubscribe command.")
    chat_id = update.effective_chat.id

    if 'chats' in context.bot_data and chat_id in context.bot_data['chats']:
        context.bot_data['chats'].remove(chat_id)
        await update.message.reply_text("You've been unsubscribed from daily random entries.")
        logger.info("Successfully removed chat from subscribers.")
    else:
        await update.message.reply_text("You weren't subscribed to daily random entries.")
        logger.info("Chat wasn't in subscribers.")
