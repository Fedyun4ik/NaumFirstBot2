import telebot

# from telebot import apihelper
# apihelper.proxy = {'https':'socks5://userproxy:password@134.209.255.141:1080'}

bot = telebot.TeleBot("801548460:AAEAX7uxD9ElwqGGNSTn5FCejWouC9BcwL8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=["text"])
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True, interval=0)
