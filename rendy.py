# credits by @FFmpegNotInstalled
# DON'T REMOVE CREDITS FUCK
# YOUR CODE NOOB ?
import audioop
import os
from telebot import *

TOKEN = "1943236911:AAHM2v3QDW3MrFN7DrN_Q7uvHW07x-wUtt8"
bot = TeleBot(TOKEN)

telebot.logger.setLevel(logging.DEBUG) 

@bot.message_handler(commands=['start'])
def welcome(message):
	me = message.from_user.id
	user = message.from_user.first_name
	fuck = message.from_user.last_name
	chatid = message.chat.id
	bot.send_message(chatid, "Name : {}\n{}ID Hack : {}\nSelamat datang!".format(user,fuck,me))

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "why helping")

@bot.message_handler(commands=['photo'])
def send_photo(message):
	bot.send_photo(message.chat.id, open('media/photo.jpg', 'rb'))

@bot.message_handler(commands=['audio'])
def send_audio(message):
	bot.send_audio(message.chat.id, open('audio/audio.mp3', 'rb'))


@bot.message_handler(commads=['kontol'])
def kontol_message(message):
        bot.send_message(message.chat.id, "tolol lu muka kek kontol")

apakah = [
       "komtol",
       "ga nanya",
       "mmksut",
       "hah",
       "anak goblok"

]

bagi = [
       "link @bokepindo",
       "link2 @hentai",
       "link3 @pornchannel",
       "link4 @indiporn",
       "link5 @sugiono"

]

@bot.message_handler(commands=['apakah'])
def apakah_ask(message):
  chatid = message.chat.id
  bot.send_message(chatid, apakah)

@bot.message_handler(commands=['bagi'])
def bagi_ask(message):
  chatid = message.chat.id
  bot.send_message(chatid, bagi)

@bot.message_handler(commands=['bokep'])
def bokep_message(message):
  chatid = message.chat.id
  bot.send_message(chatid, "nih link @bokepindo")

# stringsList = {"Name": "Rendy", "languagues": "Python", "API": "pyTelegramBotAPI"}
# crossIcon = u"\u274c"

@bot.message_handler(commands=['wsb'])
def get_stocks(message):
  response = ""
  stocks = ['gme', 'amc', 'nok']
  stock_data = []
  for stock in stocks:
    data = yf.download(tickers=stock, period='2d', interval='1d')
    data = data.reset_index()
    response += f"-----{stock}-----\n"
    stock_data.append([stock])
    columns = ['stock']
    for index, row in data.iterrows():
      stock_position = len(stock_data) - 1
      price = round(row['Close'], 2)
      format_date = row['Date'].strftime('%m/%d')
      response += f"{format_date}: {price}\n"
      stock_data[stock_position].append(price)
      columns.append(format_date)
    print()

  response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
  for row in stock_data:
    response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
  response += "\nStock Data"
  print(response)
  bot.send_message(message.chat.id, response)

def stock_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "price":
    return False
  else:
    return True

@bot.message_handler(func=stock_request)
def send_price(message):
  request = message.text.split()[1]
  data = yf.download(tickers=request, period='5m', interval='1m')
  if data.size > 0:
    data = data.reset_index()
    data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
    data.set_index('format_date', inplace=True)
    print(data.to_string())
    bot.send_message(message.chat.id, data['Close'].to_string(header=False))
  else:
    bot.send_message(message.chat.id, "No data!?")

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
print("Bot Running")
bot.polling()
