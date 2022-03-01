# Please, work! / Работай, пожалуйста!

import telebot

from markups import *
from questions import *
from tgconfig import *

telebot.apihelper.ENABLE_MIDDLEWARE = True
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60
tgbot = telebot.TeleBot(TOKEN)


@tgbot.message_handler(commands=['start'])
def welcome(message):
    sti = open('img/welcome.webp', 'rb')
    tgbot.send_sticker(message.chat.id, sti)
    tgbot.send_message(message.chat.id, (
        "Привет, {0.first_name}!\n Я - <b>{1.first_name}</b>."
        "\n Я буду оповещать тебя об изменениях в твоём школьном расписании, "
        "а также о появляющемся Д/З."
    ).format(message.from_user, tgbot.get_me()), reply_markup=startmarkup, parse_mode='html')


@tgbot.message_handler(commands=['admin'])
def test(message):
    if (message.chat.id in spb_nevs_school569__admins):
        tgbot.send_message(message.chat.id, "Done".format(
            message.from_user,
            tgbot.get_me()),
                           parse_mode='html', reply_markup=adminmarkup)
    else:
        tgbot.send_message(message.chat.id, 'Я не знаю что ответить')


@tgbot.message_handler(content_types=['text'])
def talking(message):
    if message.chat.type == 'private':
        if message.text == 'Узнать id чата':
            tgbot.send_message(message.chat.id,
                               ("id нашего с тобой чата: <b>" + str(
                                   message.chat.id) + "</b>").format(message.from_user,
                                                                     tgbot.get_me()),
                               parse_mode='html')
        elif message.text in timetablenow:
            tgbot.send_message(message.chat.id, (
                    f"Вот расписание уроков на сегодня: \n" + senttimetable('now')).format(
                message.from_user, tgbot.get_me()), reply_markup=startmarkup, parse_mode='html')
        elif message.text in timetabletomorow:
            tgbot.send_message(message.chat.id,
                               ("Вот расписание уроков на завтра: \n" + senttimetable(
                                   'tomorrow')).format(
                                   message.from_user, tgbot.get_me()), reply_markup=startmarkup,
                               parse_mode='html')
        elif message.text in botstop and message.chat.id in spb_nevs_school569__admins:
            tgbot.send_message(message.chat.id,
                               'Принято, бот успешно остановлен!'.format(message.from_user,
                                                                         tgbot.get_me()),
                               parse_mode='html')
            sti = open('img/stop.webp', 'rb')
            tgbot.send_sticker(message.chat.id, sti)
            print(f'Бот остановлен по прозьбе администратора, его id: {message.chat.id}')
            tgbot.polling(none_stop=False)
            exit(0)
        elif message.text in botgetip and message.chat.id in spb_nevs_school569__admins:
            tgbot.send_message(message.chat.id,
                               (f'Вот ip адресс бота: {getbotip()}').format(message.from_user,
                                                                            tgbot.get_me()),
                               parse_mode='html')
        else:
            tgbot.send_message(message.chat.id, 'Я не знаю что ответить')


# # looping tgBot
# while True:
#     try:
#         tgbot.polling(none_stop=True)
#     except Exception as e:
#         t.sleep(15)

tgbot.polling(none_stop=True)
