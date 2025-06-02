"""
Telegram bot scheduled job functions.
"""
from telegram.ext import ContextTypes
import jmdict


async def send_random_entry_to_all(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random entry to all registered chats."""
    entry = jmdict.get_random_jmdict_entry()
    entry = jmdict.format_jmdict_entry(entry)

    if 'chats' in context.bot_data:
        for chat_id in context.bot_data['chats']:
            await context.bot.send_message(chat_id=chat_id, text=entry)
