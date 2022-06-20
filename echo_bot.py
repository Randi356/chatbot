import telebot
import time
import urllib

url='http://scontent-b.cdninstagram.com/hphotos-xfa1/t51.2885-15/e15/10919672_584633251672188_179950734_n.jpg'
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(url).read())
f.close()

bot = telebot.TeleBot("YOUR_TOKEN_BOTFATHER")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
