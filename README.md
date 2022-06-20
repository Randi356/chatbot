# TELEBOT & PYROGRAM
code by @FFmpegNotInstalled


# CODE PYROGRAM

```console
@bot.on_message(filters.commad('start') & filters.private)
def commad1(bot, message):
    bot.send_message(message.chat.id "Hello Test")
```
