#описание https://prognote.ru/web-dev/back-end/basics-of-creating-a-telegram-bot-in-python/#:~:text=%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20Telegram%20%D0%B1%D0%BE%D1%82%D0%B0%3A%20%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC%2C,%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B8%2C%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D1%8D%D1%82%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D0%B5%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD

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

def create_keyboard():
    # Создаём тип для кнопок
    keyboard = types.InlineKeyboardMarkup()
    # Создаём первую кнопку
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data="1")
    # Создаём вторую кнопку
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data="2")
    # Добавляем первую кнопку в специальный список
    keyboard.add(drink_btn)
    # Добавляем вторую кнопку в специальный список
    keyboard.add(eat_btn)
    # Возвращаем кнопки
    return keyboard

# Обозначаем чтобы функция срабатывала при команде /start
@bot.message_handler(commands=['start'])
# Объявляем функцию
def start_bot(message):
    # Создаём кнопки
    keyboard = create_keyboard()
    # Отправляем сообщение пользователю
    bot.send_message(
        message.chat.id, # Идентификатор ID
        "Добрый день, чего хотите?", # Текст сообщения
        reply_markup=keyboard # Кнопки
    )

# Декоратор который означает для получения каких-то значений
@bot.callback_query_handler(func=lambda call: True)
# Создаём функцию
def callback_inline(call):
    # Делаем кнопки
    keyboard = create_keyboard()
    # Проверяем есть ли сообщение
    if call.message:
        # Если значение кнопки равно одному то
        if call.data == "1":
            # Открываем картинку с водой
            print(f'Здесь картинка')


        elif call.data == "2": #Если значение равно двум то
            # Открываем картинку с блинчиками
            print(f'Здесь картинка2')

if __name__ == '__main__':
    bot.polling(none_stop=True)