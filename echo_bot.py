
# credits by @FFmpegNotInstalled
# you fork editing // don't remove
import telebot
import os
import pafy

bot = telebot.TeleBot("1943236911:AAHM2v3QDW3MrFN7DrN_Q7uvHW07x-wUtt8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "i'am developer @FFmpegNotInstalled")

@bot.message_handler(commands=['link'])
def link(message):
        bot.send_message(message.chat.id, "Link https://t.me/pantekyks")

@bot.message_handler(commands=['photo'])
def send_photo(message):
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('https://images.app.goo.gl/PfE4q3rgnHnYAWix6', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

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

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
