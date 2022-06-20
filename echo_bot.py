
# credits by @FFmpegNotInstalled
# you fork editing // don't remove
from telebot import *
#from youtubesearchpython import VideoSearch
import os
import pafy
import logging
import random
import urllib3.request

# display errors 
telebot.logger.setLevel(logging.DEBUG) 

api = "1943236911:AAHM2v3QDW3MrFN7DrN_Q7uvHW07x-wUtt8"
bot = TeleBot(api)

url = 'http://scontent-b.cdninstagram.com/hphotos-xfa1/t51.2885-15/e15/10919672_584633251672188_179950734_n.jpg'
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(url).read())
f.close()

def listener(*messages):
    for m in messages:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text
            msgid = m.message_id
            if text.startswith('/photo'):
                bot.send_chat_action(chat_id, 'upload_photo')
                img = open('out.jpg', 'rb')
                bot.send_photo(chat_id, img, reply_to_message_id=msgid)
                img.close()

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
bot.set_update_listener(listener)
bot.polling()
while True:
    time.sleep(1)
