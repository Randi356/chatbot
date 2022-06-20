import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commads=['test'])
def test(message):
  bot.reply_to(message, "hello test")

bot.polling()
