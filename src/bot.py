from dotenv import load_dotenv
import os
import datetime

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, JobQueue

import jmdict


load_dotenv()


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


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


async def random_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    entry = jmdict.get_random_jmdict_entry()
    entry = jmdict.format_jmdict_entry(entry)
    await update.message.reply_text(entry)


async def send_random_entry_to_all(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random entry to all registered chats."""
    entry = jmdict.get_random_jmdict_entry()
    entry = jmdict.format_jmdict_entry(entry)

    if 'chats' in context.bot_data:
        for chat_id in context.bot_data['chats']:
            await context.bot.send_message(chat_id=chat_id, text=entry)


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


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    job_queue = application.job_queue
    job_queue.run_daily(send_random_entry_to_all,
                        time=datetime.time(hour=14, minute=10, second=0),
                        days=(0, 1, 2, 3, 4, 5, 6))

    application.add_handler(CommandHandler("subscribe", subscribe))
    application.add_handler(CommandHandler("unsubscribe", unsubscribe))

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("random", random_entry))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()