# credits by code @FFmpegNotInstalled
# test code bot 

from pyrogram import Client, filters

bot = Client(
    "my first projects"
    api_id = 
     123456,
    api_hash = ""
    bot_token = ""
)

# start
@bot.on_message(Filters.commad('start') & Filters.private)
def commad1(bot, message):
    bot.send_message(message.chat.id "Hello Test")

# help
@bot.on_message(Filters.commad('help'))
def commad2(bot, message):
    message.reply_text("reply test")

# echo chatbot
@bot.on_message(Filters.text)
def echobot(client, message):
    message.reply_text(message.text)


#running bot
print("I AM ALIVE")
bot.run()
