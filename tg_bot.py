
# Done! Congratulations on your new bot. You will find it at
# t.me/yand_notification_bot.
# You can now add a description, about section and profile picture
# for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a ' \
#         'better username for it. Just make sure the bot is fully operational before you do this.
# Use this token to access the HTTP API:
# 5429523487:AAEe5V8eHBncO_t1w-wjvXTe1Ml_GtdOofY
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

token = '5429523487:AAEe5V8eHBncO_t1w-wjvXTe1Ml_GtdOofY'
# Подключаем Telegram API
import telebot
# Подключаем библиотеку для создания кнопок
from telebot import types

token = 'Ваш_токен'
# Объявляем бота
bot = telebot.TeleBot(token)
print(bot)