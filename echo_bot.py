import telebot

bot = telebot.TeleBot("1943236911:AAHM2v3QDW3MrFN7DrN_Q7uvHW07x-wUtt8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
