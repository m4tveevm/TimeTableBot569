import sqlite3
import config
import datetime
from telegram import ReplyKeyboardMarkup


async def connect_db(request, sql_file=config.DEFAULT_SQL):
    # Функция, которая упрощает соединение с DB.
    # А, как следствие, уменьшает количество требуемых строчек кода, для реализации
    # запроссов к db.
    try:
        con = sqlite3.connect(sql_file)
        cur = con.cursor()
        result = cur.execute(f'''{request}''').fetchall()
        con.commit()
        con.close()
        return result
    except Exception as ex:
        print(ex)


async def to_day(day=''):
    if day == '':
        # обязательно не просто if not day:, тк я еще и 0 использую
        day = datetime.datetime.now()
    else:
        day = datetime.datetime.now() + datetime.timedelta(days=int(day))
    return int(day.strftime('%w'))


async def to_day_week(day):
    days = ["воскресенье", "понедельник", "вторник", "среду", "четверг", "пятницу", "субботу"]
    return days[day % 7]


async def get_class_id(user):
    return (await connect_db(f'SELECT class from users where tg_id = {user.id}'))[0][0]


async def is_user(user):
    if await connect_db(f'''SELECT name, class FROM users where tg_id = {user.id};'''):
        name, user_class = (await connect_db(f'''SELECT name, class FROM users where tg_id ={user.id};'''))[0]
        if not user_class:
            return 'wait'
        else:
            return 'done'
    else:
        name = '' if not user.name else user.name
        await connect_db(f'''INSERT INTO users (tg_id, name)
                  VALUES ('{user.id}','{name}');''')
        return None


async def make_time_table(user_class, day):
    day = day % 7
    data = [f'Вот расписание на {await to_day_week(day)}:', '\n']
    if (await connect_db(f'''SELECT subject.name FROM class left join subject on
     subject.class_id = class.id left join schedule on subject.id = schedule.subject_id where subject.class_id =
      {user_class} and schedule.day_of_week = {day} order by schedule.lesson_number''')):
        for n, lesson in enumerate((await connect_db(f'''SELECT subject.name FROM class left join subject on
         subject.class_id = class.id left join schedule on subject.id = schedule.subject_id where subject.class_id =
          {user_class} and schedule.day_of_week = {day} order by schedule.lesson_number'''))):
            data.append(f'{n + 1}. {lesson[0]}')
    else:
        data.append('К сожалению, расписания на данный день не найдено.')
    return '\n'.join(data)


# default markup
default_commands = [['на сегодня', 'на завтра'],
                    ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']]
default_keyboard = ReplyKeyboardMarkup(default_commands, one_time_keyboard=True)
