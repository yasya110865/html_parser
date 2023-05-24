import telebot
from news_func import newsparser

TOKEN = '6044805267:AAHsTIfVbVfmIRu9ifZtj2IhiagTTr5Ree0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, это новости из мира микробиологов!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "О чем хочешь узнать? Введи ключевое слово.")

@bot.message_handler(content_types=['text'])
def search_news(message):
    text = newsparser(message.text)

    for i in range(len(text)):
        bot.send_message(message.chat.id, text[i])


bot.polling()