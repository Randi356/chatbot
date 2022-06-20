
# credits by @FFmpegNotInstalled
# you fork editing // don't remove
from telebot import *
import os
import pafy

api = "1943236911:AAHM2v3QDW3MrFN7DrN_Q7uvHW07x-wUtt8"
bot = TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "i'am developer @FFmpegNotInstalled")

@bot.message_handler(commands=['link'])
def link(message):
        bot.send_message(message.chat.id, "Link https://t.me/pantekyks")

@bot.message_handler(commands=['audio'])
def send_audio(message):
        url = pafy.new(message.text.replace("/mp3", ""))
        bot.send_message(message.chat.id, url.title)
        bot.send_message(message.chat.id, "Please Wait Upload....")
        fuk = url.getbestaudio()
        fuk.download(f"{url.title}.mp3")

        for i in os.listdir():
           if i.endswith(".mp3"):
               print(i)
               bot.send_audio(message.chat.id, open(i, "rb"))
               os.remove(i)

# bot run
bot.infinity_polling()
