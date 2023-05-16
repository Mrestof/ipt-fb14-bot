import json
import random

from telegram import Update
from telegram.ext import CallbackContext

from utils import diary
from utils.image import download_wallhaven, remove_file, resize_image, download_hentai
from utils.minecraft import server_stats
from utils.markov_chains import generate_markov_sentence
from utils.schedule import get_schedule

__all__ = [
    # hidden
    'ping', 'auf_markov', 'minecraft',
    # image
    'hentai', 'ero', 'ecchi', 'photo',
    # markov
    'semen_markov', 'razum_markov', 'khashcha_markov', 'bolgov_markov', 'makuha_markov',
    # diary
    'diary_write', 'diary_delete', 'diary_read_all', 'diary_remind',
    # diary hidden
    'diary_read_date',
    # schedule
    'schedule_today', 'schedule_tomorrow', 'schedule_this_week_day', 'schedule_next_week_day',
    # other
    'auf', 'deadinside', 'call_all',
]


async def ping(update: Update, context: CallbackContext) -> None:
    """Function for tests.

    [description]:
    [name]:ping
    [is_hidden]:True

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='pong'
    )


async def hentai(update: Update, context: CallbackContext) -> None:
    """Function to download and send Hentai mangas profile pictures and their tags.

    [description]:Відійти на 5 хвилин
    [name]:hentai
    [is_hidden]:True

    :param update:
    :param context:
    :return:
    """
    filename = download_hentai()
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(filename, 'rb'),
        caption="nhentai-" + filename
    )
    remove_file(filename)


async def ero(update: Update, context: CallbackContext) -> None:
    """Function to download and send Erotic photos and their names

    [description]:Шкіряні мішки з м`ясом
    [name]:ero
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    path = download_wallhaven('ero')
    resize_image(path, 1920)
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(path, 'rb'),
        caption=path
    )
    remove_file(path)


async def ecchi(update: Update, context: CallbackContext) -> None:
    """Function to download and send Ecchi pictures SFW

    [description]:Safe for батьки
    [name]:ecchi
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    path = download_wallhaven('ecchi')
    resize_image(path, 1920)
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(path, 'rb'),
        caption=path
    )
    remove_file(path)


async def photo(update: Update, context: CallbackContext) -> None:
    """Function to download and send Photos and their names

    [description]:Вах яка краса
    [name]:photo
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    path = download_wallhaven('photo')
    resize_image(path, 1920)
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(path, 'rb'),
        caption=path
    )
    remove_file(path)


async def auf(update: Update, context: CallbackContext) -> None:
    """Function to send quotes from real men

    [description]:АУФ
    [name]:auf
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    try:
        with open('data/pacan.txt') as f:
            lines = f.readlines()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=random.choice(lines)
        )
    except FileNotFoundError:
        print('error: data/pacan.txt does not exist')


async def minecraft(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Ваня досить ферми будувати
    [name]:minecraft
    [is_hidden]:True

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=server_stats()
    )


async def auf_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:
    [name]:auf_markov
    [is_hidden]:True

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=generate_markov_sentence('auf')
    )


async def semen_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Сем
    [name]:semen_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=generate_markov_sentence('semen') + ' (c) Семен'
    )


async def razum_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Іля Разум
    [name]:razum_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=generate_markov_sentence('razum') + ' (c) Иля'
    )


async def khashcha_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Бір
    [name]:khashcha_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=generate_markov_sentence('khashcha') + ' (c) Хаща'
    )


async def bolgov_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Коля
    [name]:bolgov_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=generate_markov_sentence('bolgov') + ' (c) Коля'
    )


async def makuha_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Негр
    [name]:makuha_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=generate_markov_sentence('makuha') + ' (c) Макуха'
    )


async def deadinside(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Я умер, прости
    [name]:deadinside
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    try:
        with open('data/deadinside.txt', 'r') as f:
            deadinside_items = list(map(str.strip, f.readlines()))
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=random.choice(deadinside_items)
        )
    except FileNotFoundError:
        print('error: data/deadinside.txt does not exist')


async def call_all(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Закликати всіх нагору!
    [name]:call_all
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    allowed_users = [1399469085]  # toconf
    if update.message.from_user.id not in allowed_users:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Вам не дозволено викликати цю команду'
        )
        return None

    try:
        with open('data/userids.txt', 'r') as f:
            userids = map(str.strip, f.readlines())
        userstring = ''
        for userid in userids:
            userstring += fr'[\|](tg://user?id={userid})'
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Заклик ФБ14\n' + userstring,
            parse_mode='MarkdownV2'
        )
    except FileNotFoundError:
        print('error: data/userids.txt does not exist')


async def diary_read_date(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Щоденник-1
    [name]:diary_read_date
    [is_hidden]:True

    :param update:
    :param context:
    :return:
    """

    if len(context.args) == 1:
        date = context.args[0]
        response = diary.read_one_date(date)
    else:
        response = 'Потрібно 1 аргумент'

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response,
        reply_to_message_id=update.message.message_id
    )


async def diary_read_all(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Щоденник-4
    [name]:diary_read_all
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=diary.read_full(),
        reply_to_message_id=update.message.message_id
    )


async def diary_write(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Щоденник-2
    [name]:diary_write
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """

    try:
        with open('data/userids.txt', 'r') as f:
            userids = map(str.strip, f.readlines())

        if str(update.message.from_user.id) not in userids:
            response = 'Вам не дозволено викликати цю команду'
        elif len(context.args) >= 2:
            date = context.args[0]
            text = ' '.join(context.args[1:])
            response = diary.write_one_note(date, text)
        else:
            response = 'Потрібно 2 аргументи'

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response,
            reply_to_message_id=update.message.message_id
        )
    except FileNotFoundError:
        print('error: data/userids.txt does not exist')


async def diary_delete(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Щоденник-3
    [name]:diary_delete
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """

    try:
        with open('data/userids.txt', 'r') as f:
            userids = list(map(str.strip, f.readlines()))

        if str(update.message.from_user.id) not in userids:
            response = 'Вам не дозволено викликати цю команду'
        elif len(context.args) == 2:
            date = context.args[0]
            number = context.args[1]
            response = diary.delete_one_note(date, number)
        else:
            response = 'Потрібно 2 аргументи'

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response,
            reply_to_message_id=update.message.message_id
        )
    except FileNotFoundError:
        print('error: data/userids.txt does not exist')


async def diary_remind(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Вимкає або вимикає нагадування про записи в щоденнику
    [name]:diary_remind
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    try:
        used_id = update.message.from_user.id
        with open('data/diary_remind.json', 'r') as f:
            diary_remind_users: list = json.load(f)

        if used_id not in diary_remind_users:
            diary_remind_users.append(used_id)
            with open('data/diary_remind.json', 'w') as f:
                json.dump(diary_remind_users, f)
            response = 'Вас тепер буде тегати за день до записів'

        else:
            diary_remind_users.remove(used_id)
            with open('data/diary_remind.json', 'w') as f:
                json.dump(diary_remind_users, f)
            response = 'Вас тепер не буде тегати за день до записів'

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response,
            reply_to_message_id=update.message.message_id
        )
    except FileNotFoundError:
        print('error: data/diary_remind.json does not exist')


async def schedule_today(update: Update, context: CallbackContext) -> None:
    """Function to get schedule for today

    [description]:Розклад на сьогодні
    [name]:schedule_today
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_schedule(),
        disable_web_page_preview=True,
    )


async def schedule_tomorrow(update: Update, context: CallbackContext) -> None:
    """Function to get schedule for tomorrow

    [description]:Розклад на завтра
    [name]:schedule_tomorrow
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_schedule(is_next_day=True),
        disable_web_page_preview=True,
    )


async def schedule_this_week_day(update: Update, context: CallbackContext) -> None:
    """Function to get schedule for this week's day

    [description]:Розклад дня на цьому тижні
    [name]:schedule_this_week_day
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    if len(context.args) > 0:
        day = context.args[0]

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=get_schedule(day=day),
            disable_web_page_preview=True,
        )

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Потрібно 1 аргумент - день тижня',
            reply_to_message_id=update.message.message_id
        )


async def schedule_next_week_day(update: Update, context: CallbackContext) -> None:
    """Function to get schedule for next week's day

    [description]:Розклад дня з наступного тижня
    [name]:schedule_next_week_day
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    if len(context.args) > 0:
        day = context.args[0]

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=get_schedule(day=day, is_this_week=False),
            disable_web_page_preview=True,
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Потрібно 1 аргумент - день тижня',
            reply_to_message_id=update.message.message_id
        )
