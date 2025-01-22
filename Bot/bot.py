import telebot

bot = telebot.TeleBot('8093831394:AAFl7Zs1GzyRiUVWrAbC7AaQIrUSKUQkZcQ')

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Hellow")

bot.polling(non_stop=True)
