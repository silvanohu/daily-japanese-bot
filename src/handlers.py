"""
Telegram bot command and message handlers.
"""
from telegram import ForceReply, Update
from telegram.ext import ContextTypes
import jmdict


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def random_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random JMDict entry to the user."""
    entry = jmdict.get_random_jmdict_entry()
    entry = jmdict.format_jmdict_entry(entry)
    await update.message.reply_text(entry)


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add the chat to daily notifications."""
    chat_id = update.effective_chat.id

    if 'chats' not in context.bot_data:
        context.bot_data['chats'] = set()

    context.bot_data['chats'].add(chat_id)
    await update.message.reply_text("You've been subscribed to daily random entries!")


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove the chat from daily notifications."""
    chat_id = update.effective_chat.id

    if 'chats' in context.bot_data and chat_id in context.bot_data['chats']:
        context.bot_data['chats'].remove(chat_id)
        await update.message.reply_text("You've been unsubscribed from daily random entries.")
    else:
        await update.message.reply_text("You weren't subscribed to daily random entries.")
