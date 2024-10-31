from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import telebot
from captura_UIM import register_uim_commands
from captura_grafana import register_grafana_commands
from captura_APM import register_apm_commands

TOKEN = '7334401995:AAHHhaXJYn6hpZzP7OJrpOTdDyxULc7Epug'

bot = telebot.TeleBot(TOKEN)

#se hace la llamada a los comandos desde captura_grafan y captura_UIM.
#register_media_commands(bot)
#register_capture_commands(bot)
register_grafana_commands(bot)
register_uim_commands(bot)
register_apm_commands(bot)

@bot.message_handler(func= lambda message : True)
def echo_all(message):
    bot.reply_to(message, message.text) 
bot.infinity_polling()