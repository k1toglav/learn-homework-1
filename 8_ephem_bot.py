"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
from ephem import *

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
  print('Вызван /start')
  update.message.reply_text('Здравствуй, пользователь')

def call_planet(update, context):
  print('Вызвана команда /planet')
  update.message.reply_text('Введите название планеты на английском языке ')
  planet_name = update.message.text.split()
  planet_name = planet_name[0]
  print(planet_name)
  answer = constellation(planet_name, ('2022'))
  print(answer)
  update.message.reply_text(answer)

def main():
  mybot = Updater(settings.API_KEY, use_context=True)

  dp = mybot.dispatcher
  dp.add_handler(CommandHandler('start', greet_user))
  dp.add_handler(CommandHandler('planet', call_planet))
  dp.add_handler(MessageHandler(Filters.text, greet_user))
  dp.add_handler(MessageHandler(Filters.text, call_planet))

  logging.info('Bot started')

  mybot.start_polling()
  mybot.idle()

main()