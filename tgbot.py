# Работай пожалуйста
import telebot
from telebot import types
from datetime import datetime
# pip install pyTelegramBotAPI

# import config
import tgconfig
from tgconfig import *
tgbot = telebot.TeleBot(tgconfig.TOKEN)

# Markups
startmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
KeyBoardSettings = types.KeyboardButton("🔧 Настройки")
KeyBoardStats = types.KeyboardButton("📈 Статус бота")
startmarkup.add(KeyBoardSettings, KeyBoardStats)

# reply_markup=startmarkup


#
timetablenow = ['Расписание', 'расписание', 'уроки', 'сегодня']
timetabletomorow = ['завтра', 'делать', 'Завтра']
botstop = ['Стоп', 'стоп']


@tgbot.message_handler(commands=['start'])
def welcome(message):
    sti = open('img/welcome.webp', 'rb')
    tgbot.send_sticker(message.chat.id, sti)

    tgbot.send_message(message.chat.id, (
        "Привет, {0.first_name}!\n Я - <b>{1.first_name}</b>. "
        "\n Я буду оповещать тебя об изменениях в твоём школьном расписании, а также о появляющемся Д/З."
    ).format(message.from_user, tgbot.get_me()), parse_mode='html')


@tgbot.message_handler(commands=['admin'])
def test(message):
    if (message.chat.id == 505848766):
        tgbot.send_message(message.chat.id,
                           ("Добрый день, {0.first_name}! id нашего чата:", message.chat.id).format(message.from_user,
                                                                                                    tgbot.get_me()),
                           parse_mode='html')
    else:
        tgbot.send_message(message.chat.id,
                           ("{0.first_name}, ты не являешься моим администратором. " + str(message.chat.id)).format(
                               message.from_user, tgbot.get_me()), parse_mode='html')


@tgbot.message_handler(content_types=['sticker'])
def checksticer(message):
    tgbot.send_message(message.chat.id, ('id стикера: ', sticker.chat.id).format(
        message.from_user, tgbot.get_me()), parse_mode='html')


@tgbot.message_handler(content_types=['text'])
def talking(message):
    if message.chat.type == 'private':
        if message.text == ('🔧 Настройки' or 'Настройки' or 'настройки'):
            tgbot.send_message(message.chat.id,
                               ("Вы находитесь в меню настроек <b> </b> Что выхотите изменить?").format(
                                   message.from_user, tgbot.get_me()), parse_mode='html')
        elif message.text == ('📈 Статус бота' or 'статус' or 'Статус' or 'статус бота' or 'Статус бота'):
            tgbot.send_message(message.chat.id, 'В данный момент бот online'.format(message.from_user, tgbot.get_me()),
                               parse_mode='html')
        elif message.text == '🏠 Главное меню':
            tgbot.send_message(message.chat.id,
                               'Сейчас вы находитесь в главном меню <b> </b> Чем я могу помочь?'.format(
                                   message.from_user, bot.get_me()), parse_mode='html')
        elif message.text == 'Узнать id чата':
            tgbot.send_message(message.chat.id,
                               ("id нашего с тобой чата: <b>" + str(message.chat.id) + "</b>").format(message.from_user,
                                                                                                      tgbot.get_me()),
                               parse_mode='html')
        elif message.text in timetablenow:
            tgbot.send_message(message.chat.id, (f"Вот расписание уроков на сегодня: \n" + senttimetable('now')).format(
                message.from_user, tgbot.get_me()), parse_mode='html')
        elif message.text in timetabletomorow:
            tgbot.send_message(message.chat.id,
                               ("Вот расписание уроков на завтра: \n" + senttimetable('tomorrow')).format(
                                   message.from_user, tgbot.get_me()), parse_mode='html')
        elif message.text in botstop and message.chat.id in spb_nevs_school569__admins:
            tgbot.send_message(message.chat.id,
                               'Принято, бот успешно остановлен!'.format(message.from_user, tgbot.get_me()),
                               parse_mode='html')
            sti = open('img/stop.webp', 'rb')
            tgbot.send_sticker(message.chat.id, sti)
            print(f'Бот остановлен по прозьбе администратора, его id: {message.chat.id}')
            print(1 / 0)
        else:
            tgbot.send_message(message.chat.id, 'Я не знаю что ответить')


# looping tgBot
tgbot.polling(none_stop=True, interval=0)
