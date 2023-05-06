import logging
from tools import *
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler

from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)


async def admin(update, context):
    admin_commands = [['/add_users', ''],
                      ['', '']]
    admin_keyboard = ReplyKeyboardMarkup(admin_commands, one_time_keyboard=True)
    await update.message.reply_text('Выполнено, выдал вам клавиатуру администратора'
                                    '', reply_markup=admin_keyboard)


async def important_numbers(update, context):
    await update.message.reply_text('Выполнено, выдал вам клавиатуру администратора'
                                    '', reply_markup=default_keyboard)


async def add_users(update, context):
    # Оповещает пользователей, которых добавили в bd в какой-то класс.
    users = await connect_db('''SELECT tg_id FROM users where update_form = 1''')
    for user_id in users:
        user_class, user_school = (await connect_db(f'''SELECT class.name, schools.name FROM users left join class 
        on users.class = class.id left join schools on class.school_id = schools.id where tg_id = {user_id[0]}'''))[0]
        if user_class is None or user_school is None:
            continue
        await context.bot.send_message(chat_id=user_id[0], text=f"""
Верификация пройдена! Образовательная площадка:
"{user_school}" приняла тебя в своей системе. 
Теперь у тебя есть доступ функционалу твоего класса: "{user_class}"!""")
        await connect_db(f'''UPDATE users
        SET update_form = 0
        WHERE tg_id = {user_id[0]} ''', )
    if len(users) > 0:
        await update.message.reply_text(f'Выполнено, оповестил всех новых учеников. ({len(users)} человек)')
    else:
        await update.message.reply_text(f'Запрос был выполнен, но нашлось лишь {len(users)} человек')


async def start(update, context):
    user = update.effective_user
    if await is_user(user):
        if await is_user(user) == "wait":
            await update.message.reply_html(rf"""Привет {user.mention_html()}!
Твоя заявка {user.id} находится на рассмотрении.""")
        elif await is_user(user) == 'done':
            await update.message.reply_html(rf"""{user.mention_html()}, вы уже прошли верификацию.""")
    else:
        await update.message.reply_html(f"""Привет {user.mention_html()}!
Для продолжения нашего взаимодействия, попроси куратора твоего образовательного учреждения добавить 
тебя в нашу платформу. Не забудь указать id своего обращения(id: {user.id}) либо свой telegram id""")


async def token_connection(update, context):
    token = context.args
    if len(token) == 1:
        if token[0].isdigit():
            if await connect_db(f'''SELECT class_id 
    FROM tokens
    WHERE token_id = {token[0]};'''):
                class_id = (await connect_db(f'''SELECT class_id 
            FROM tokens
            WHERE token_id = {token[0]};'''))[0][0]
                await connect_db(f'''UPDATE users
                        SET class = {class_id}
                        WHERE tg_id = {update.effective_user.id} ''')
                user_class, user_school = (await connect_db(f'''SELECT class.name, schools.name FROM users left join 
            class on users.class = class.id left join schools on class.school_id = schools.id where tg_id = 
    {update.effective_user.id}'''))[0]
                await update.message.reply_text(f"""
Верификация пройдена! Образовательная площадка:
"{user_school}" приняла тебя в своей системе. 
Теперь у тебя есть доступ функционалу твоего класса: "{user_class}"!""", reply_markup=default_keyboard)
            else:
                await update.message.reply_text('''
                        Ошибка, такого токена я не знаю, проверь, токен должен быть введен в одну строчку:
пример /token number
Где number - число, в вашем случае, number не являлся числом.''')

    elif token:
        await update.message.reply_text('''
        Ошибка, такого токена я не знаю, проверь, токен должен быть введен в одну строчку:
пример /token number
Обратите внимание на написание токена в одну строчку!''')
    else:
        await update.message.reply_text('''
                Ошибка, такого токена я не знаю, проверь, токен должен быть введен в одну строчку:
пример /token number
К сожалению вы отправили пустой токен.''')


async def today(update, context):
    user = update.effective_user
    await update.message.reply_text(await make_time_table(await get_class_id(user), await to_day()),
                                    reply_markup=default_keyboard)


async def tomorrow(update, context):
    user = update.effective_user
    await update.message.reply_text(await make_time_table(await get_class_id(user), await to_day() + 1),
                                    reply_markup=default_keyboard)


async def dep_to(update, context):
    message = context.args
    if len(message) >= 2:
        print(message)
        if ':' not in update.message.text:
            await update.message.reply_text('''Ошибка, такого запроса я не знаю.
Проверьте, написание сообщения для обучающихся по шаблону /dep_to {класс/классы}: {сообщение}

Пример: /dep_to 11А: Завтра будет олимпиада!

Для оповещения сразу всех учеников используйте команду /dep_to all: {сообщение}
Пример: /dep_to all: Наша школа самая сильная!
В вашем запросе не нашёлся символ ":"''')
            return None
        else:
            class_alt_name = update.message.text.replace('/dep_to ', '', 1).replace(' ', '').split(':')[0].split(',')
            class_alt_name[-1] = class_alt_name[-1].replace(':', '', 1)
            user_school = (await connect_db(f'''SELECT schools.id FROM users 
left join class on users.class = class.id 
left join schools on class.school_id = schools.id
where users.tg_id = {update.effective_user.id}'''))[0][0]
            if len(class_alt_name) == 1:
                class_alt_name = list(class_alt_name)
            if class_alt_name[0].lower() == 'all':
                class_alt_name = list(await connect_db(f'''SELECT class.local_alt_name FROM users 
left join class on users.class = class.id 
left join schools on class.school_id = schools.id
where schools.id = {user_school}'''))
            class_alt_name = set(class_alt_name)
            print(class_alt_name)
            for class_id in class_alt_name:
                if class_id:
                    if len(class_id[0]) > 1:
                        class_id = class_id[0]
                    print(class_id)
                    is_error = False
                    if not (await connect_db(f'''SELECT tg_id FROM users 
    left join class on users.class = class.id 
    left join schools on class.school_id = schools.id
    where schools.id = {user_school} and class.local_alt_name = '{class_id}'
                    ''')):
                        if not is_error:
                            is_error = True
                            await update.message.reply_text(
                                f'Не удалось отправить оповещение, так как "{class_id}" класс отсутствует в системе')
                    for user_id in (await connect_db(f'''SELECT tg_id FROM users 
    left join class on users.class = class.id 
    left join schools on class.school_id = schools.id
    where schools.id = {user_school} and class.local_alt_name = '{class_id}'
                    ''')):
                        user_id = user_id[0]
                        message = update.message.text.replace('/dep_to', 'to', 1)
                        await context.bot.send_message(chat_id=user_id, text=f"Сообщение от {user_id}:\n{message}")
    else:
        await update.message.reply_text('''Ошибка, такого запроса я не знаю.
Проверьте, написание сообщения для обучающихся по шаблону /dep_to {класс/классы}: {сообщение}

Пример: /dep_to 11А: Завтра будет олимпиада!

Для оповещения сразу всех учеников используйте команду /dep_to all: {сообщение}
Пример: /dep_to all: Наша школа самая сильная!''')


async def text(update, context):
    user = update.effective_user
    if await is_user(user) != 'done':
        await start(update, context)
    else:
        if update.message.text.lower() in ['на сегодня', 'сегодня', 'сейчас', 'расписание']:
            await update.message.reply_text(await make_time_table(await get_class_id(user), await to_day()),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() in ['на завтра', 'завтра']:
            await update.message.reply_text(await make_time_table(await get_class_id(user), (await to_day() + 1)),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() == 'воскресенье':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 0),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() == 'понедельник':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 1),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() == 'вторник':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 2),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() == 'среда':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 3),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() == 'четверг':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 4),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() == 'пятница':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 5),
                                            reply_markup=default_keyboard)
        elif update.message.text.lower() == 'суббота':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 6),
                                            reply_markup=default_keyboard)
        else:
            await update.message.reply_text('Я не совсем понимаю', reply_markup=default_keyboard)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, text)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin", admin))
    application.add_handler(CommandHandler("add_users", add_users))
    application.add_handler(CommandHandler("token", token_connection))
    application.add_handler(CommandHandler("today", today))
    application.add_handler(CommandHandler("tomorrow", tomorrow))
    application.add_handler(CommandHandler("dep_to", dep_to))
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
