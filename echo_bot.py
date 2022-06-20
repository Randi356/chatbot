
# credits by @FFmpegNotInstalled
# you fork editing // don't remove
import telebot
import time
import urllib

url='http://scontent-b.cdninstagram.com/hphotos-xfa1/t51.2885-15/e15/10919672_584633251672188_179950734_n.jpg'
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(url).read())
f.close()

bot = telebot.TeleBot("1943236911:AAHM2v3QDW3MrFN7DrN_Q7uvHW07x-wUtt8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "i'am developer @FFmpegNotInstalled")

@bot.message_handler(commands=['link'])
def link(message):
        bot.send_message(message.chat.id, "Link https://t.me/pantekyks"

@bot.message_handler(commands=['photo'])
def send_photo(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = open('out.jpg', 'rb')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    img.close()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
