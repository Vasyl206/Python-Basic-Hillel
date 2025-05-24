import telebot

token = ""

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])#Декоратор @bot.message_handler(commands=['...']) связывает команду, введённую пользователем, с определённой функцией, которая обрабатывает эту команду.
def start_message(message):#Это функуия с названием start_message с параметром message
  bot.send_message(message.chat.id,"Привет ✌️ ")#Команда, которая отправляет сообщение пользователю.
bot.infinity_polling()
@bot.message_handler(commands=["button"])
def button_message(message):

