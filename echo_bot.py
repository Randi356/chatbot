
# credits by @FFmpegNotInstalled
# you fork editing // don't remove
from telebot import *
#from youtubesearchpython import VideoSearch
import os
import pafy
import logging
import random

# display errors 
telebot.logger.setLevel(logging.DEBUG) 

api = "1943236911:AAHM2v3QDW3MrFN7DrN_Q7uvHW07x-wUtt8"
bot = TeleBot(api)

all_photo = [
    "https://telegra.ph/file/541d3310d646dadeb8341.jpg",
    "https://telegra.ph/file/434aaf1f3ee606977b8f0.jpg"
]


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "i'am developer @FFmpegNotInstalled")

@bot.message_handler(commans=['wibu'])
def wibu_message(welcome):
        while True:
            with open(random.choice(all_photo), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            photo.close()
            time.sleep(1500)

@bot.message_handler(commands=['link'])
def link(message):
        bot.send_message(message.chat.id, "Link https://t.me/pantekyks")

# youtube search old
#@bot.message_handler(commands=['mp3'])
#def send_music(message):
#        url = pafy.new(message.text.replace("/mp3 ", ""))
#        bot.send_message(message.chat.id, url.title)
#        bot.send_message(message.chat.id, "Please Wait Upload....")
#        fuk = url.getbestaudio()
#        fuk.download(f'{url.title}.mp3')
#
#        for i in os.listdir():
#           if i.endswith(".mp3"):
#               print(i)
#               bot.send_audio(message.chat.id, open(i, "rb"))
#               os.remove(i)

# fixed issue old
#@bot.message_handler(commads=['search'])
#def send_search(message):
#        data = message.text
#        video = VideoSearch(data.replace("/search ", ""),
#        limit = 3)
#        x = video.result()
#
#        for i in range(3):
#            judul = x['result'][i]['tile']
#            url = x['result'][i]['link']
#            bot.send_message(message.chat.id, judul+"\n"+url)


# bot run
bot.polling()
