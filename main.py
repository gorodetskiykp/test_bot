import logging
import telebot

from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# обработка команд - /start /help
# обработка текста
# обработка сигналов - callback - от telegram-кнопок
# вызываемые обработчики


# inline - в сообщениях
# sticky - внизу - генератор текста

# logger = telebot.logger
# logger.setLevel(logging.DEBUG)


@bot.callback_query_handler(func=lambda call: 'YesNo:' in call.data)
def save_age(call):
    bot.send_message(call.message.chat.id, call.data)


def get_age(message):
    print("get_age")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text='Да', callback_data='YesNo:yes'))
    keyboard.add(types.InlineKeyboardButton(text='Нет', callback_data='YesNo:no'))
    bot.send_message(message.chat.id, 'Да или нет?', reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
    bot.register_next_step_handler(message, get_age)


@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, 'Помоги(')


@bot.message_handler(commands=['id'])
def bot_id(message):
    bot.send_message(message.chat.id, message.chat.id)





bot.infinity_polling()
