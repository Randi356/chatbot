
# credits by @FFmpegNotInstalled
# you fork editing // don't remove
import telebot

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
        bot.send_audio(message.chat.id, 'upload_audio')
        audio = open('mp3/test.mp3', 'rb'))
        bot.send_audio(message.chat.id, audio, reply_to_message_id=message_id)
        audio.close()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
