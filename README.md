# daily-japanese-bot

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)
  - [Daily Japanese Words](#daily-japanese-words)
  - [Random Japanese Words](#random-japanese-words)
- [Usage](#usage)
  - [Try the Bot](#try-the-bot)
  - [Setting Up Your Own Instance](#setting-up-your-own-instance)
    - [Using Docker](#using-docker-recommended)
    - [Manual Setup](#manual-setup)
  - [Bot Commands](#bot-commands)
- [Contributing](#contributing)

# Introduction
daily-japanese-bot is a Telegram bot that helps users learn Japanese by providing daily vocabulary words. The bot utilizes the JMdict dictionary database to provide accurate Japanese-English translations and language learning features.

# Features

## Daily Japanese Words
The bot sends scheduled daily Japanese vocabulary words to users, helping them consistently learn new words and phrases.

## Random Japanese Words
Users can request random Japanese words at any time using a command. This feature is perfect for users who want to learn more words beyond the daily scheduled word or practice at their own pace.

# Usage

## Try the Bot
You can try out the bot by searching for @daily_japanese_bot on Telegram. Start chatting with it to learn Japanese words right away!

## Setting Up Your Own Instance
1. Clone this repository
2. Download the JMdict_e file from [the official source](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) and place it in the root directory
3. You can run the bot in two ways:

### Using Docker (Recommended)
1. Create a Telegram bot and get your bot token from @BotFather
2. Build the Docker image:
   ```bash
   docker build -t daily-japanese-bot .
   ```
3. Run the container:
   ```bash
   docker run -e TELEGRAM_BOT_TOKEN="your_bot_token_here" daily-japanese-bot
   ```

### Manual Setup
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a Telegram bot and get your bot token from @BotFather
3. Set up your environment variables:
   ```bash
   export TELEGRAM_BOT_TOKEN="your_bot_token_here"
   ```
4. Run the bot:
   ```bash
   python src/bot.py
   ```

## Bot Commands
Once the bot is running, you can interact with it using these commands:
- `/start` - Begin using the bot and receive a welcome message
- `/help` - View available commands and usage information
- `/random` - Get a random Japanese word
- `/subscribe` - Subscribe to daily Japanese words
- `/unsubscribe` - Stop receiving daily Japanese words

# Contributing
Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing_feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing_feature`)
5. Open a Pull Request
