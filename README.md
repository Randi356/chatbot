# TELEBOT & PYROGRAM
`code by @FFmpegNotInstalled`


# CODE PYROGRAM

```console
@bot.on_message(filters.commad('start') & filters.private)
def commad1(bot, message):
    bot.send_message(message.chat.id "Hello Test")
```

# CODE TELEBOT API
```console
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
```
