import asyncio
import logging, sys
from tools import *
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler

from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)


async def admin(update, context):
    admin_commands = [['/add_users', '/reload'],
                      ['', '']]
    admin_keyboard = ReplyKeyboardMarkup(admin_commands, one_time_keyboard=True)
    await update.message.reply_text('Выполнено, выдал вам клавиатуру администратора', reply_markup=admin_keyboard)


async def add_users(update, context):
    # Оповещает пользователей, которых добавили в bd в какой-то класс.
    users = await connect_db('''SELECT tg_id FROM users where update_form = 1''')
    for user_id in users:
        user_class, user_school = (await connect_db(f'''SELECT class.name, schools.name FROM users left join class 
        on users.class = class.id left join schools on class.school_id = schools.id where tg_id = {user_id[0]}'''))[0]
        if user_class == None or user_school == None:
            continue
        await context.bot.send_message(chat_id=user_id[0], text=f"""
Верификация пройдена! Образовательная площадка:
"{user_school}" приняла тебя в своей системе. 
Теперь у тебя есть доступ функционалу твоего класса: "{user_class}"!""")

    await update.message.reply_text('Выполнено, оповестил всех новых учеников.')


async def start(update, context):
    user = update.effective_user
    if await is_user(user):
        if await is_user(user) == "wait":
            await update.message.reply_html(rf"""Привет {user.mention_html()}!
Твоя заявка {user.id} находится на рассмотрении.""")
        elif await is_user(user) == 'done':
            await update.message.reply_html(rf"""{user.mention_html()}, вы уже прошли верефикацию.""")
    else:
        await update.message.reply_html(f"""Привет {user.mention_html()}!
Для продолжения нашего взаимодействия, попроси куратора твоего образовательного учереждения добавть 
тебя в нашу платформу. Не забудь указать id своего обращения(id: {user.id}) либо свой telegram id""")


async def text(update, context):
    user = update.effective_user
    if await is_user(user) != 'done':
        await start(update, context)
    else:
        if update.message.text.lower() == 'на сегодня':
            await update.message.reply_text(await make_time_table(await get_class_id(user), await to_day()))
        elif update.message.text.lower() == 'на завтра':
            await update.message.reply_text(await make_time_table(await get_class_id(user), (await to_day() + 1)))
        elif update.message.text.lower() == 'воскресенье':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 0))
        elif update.message.text.lower() == 'понедельник':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 1))
        elif update.message.text.lower() == 'вторник':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 2))
        elif update.message.text.lower() == 'среда':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 3))
        elif update.message.text.lower() == 'четверг':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 4))
        elif update.message.text.lower() == 'пятница':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 5))
        elif update.message.text.lower() == 'суббота':
            await update.message.reply_text(await make_time_table(await get_class_id(user), 6))
        else:
            await update.message.reply_text('Я не совсем понимаю')


def main():
    global application
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, text)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin", admin))
    application.add_handler(CommandHandler("add_users", add_users))
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
