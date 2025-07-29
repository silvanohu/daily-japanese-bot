"""
Main Telegram bot application.
"""
from dotenv import load_dotenv
import os
import datetime

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers import start, help_command, random_entry, subscribe, unsubscribe
from scheduler import send_random_entry_to_all
from logger import setup_logging

load_dotenv()


def setup_handlers(application: Application) -> None:
    """Configure all command and message handlers."""
    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("random", random_entry))
    application.add_handler(CommandHandler("subscribe", subscribe))
    application.add_handler(CommandHandler("unsubscribe", unsubscribe))


def setup_scheduler(application: Application) -> None:
    """Configure scheduled jobs."""
    job_queue = application.job_queue
    job_queue.run_daily(
        send_random_entry_to_all,
        time=datetime.time(hour=15, minute=0, second=0),
        days=(0, 1, 2, 3, 4, 5, 6)  # All days of the week
    )


def main() -> None:
    """Start the bot."""

    # Set up logger
    logger = setup_logging(log_level=os.getenv("LOG_LEVEL", "INFO").upper())
    logger.info("Starting application.")

    # Create the Application
    logger.info("Setting up Telegram bot.")
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Setup handlers and scheduler
    logger.info("Setting up handlers and scheduler.")
    setup_handlers(application)
    setup_scheduler(application)

    logger.info("Application started successfully.")

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
