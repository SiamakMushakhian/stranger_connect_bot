import telebot
import os
from loguru import logger

class Bot():
    def __init__(self):
        self.bot = telebot.TeleBot(
            os.environ['TELEGRAMBOT_TOKEN'], 
            parse_mode=None
            ) # You can set parse_mode by default. HTML or MARKDOWN

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    def run(self):
        logger.info('Running bot ...')
        self.bot.polling()

if __name__ == '__main__':
    bot = Bot()
    bot.run()

