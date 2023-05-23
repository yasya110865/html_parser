import telebot
from news_func import newsparser

TOKEN = '6044805267:AAHsTIfVbVfmIRu9ifZtj2IhiagTTr5Ree0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, это новости из мира микробиологов!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "О чем хочешь узнать?")

bot.polling()