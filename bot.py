# credits by code @FFmpegNotInstalled
# test code bot 

from pyrogram import Client 

bot = Client(
    "my first projects"
    api_id = 
     123456,
    api_hash = ""
    bot_token = ""
)

@bot.on_message(filters.commad('start') & filters.private)
def commad1(bot, message):
    bot.send_message(message.chat.id "Hello Test")

#running bot
print("I AM ALIVE")
bot.run()
