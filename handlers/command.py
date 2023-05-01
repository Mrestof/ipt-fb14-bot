import random

from telegram import Update
from telegram.ext import CallbackContext

from utils.image import download_wallhaven, remove_file, resize_image, download_hentai
from utils.minecraft import server_stats
from utils.markov_chains import generate_markov_sentence

__all__ = [
    # hidden
    'ping', 'auf_markov', 'minecraft',
    # image
    'hentai', 'ero', 'ecchi', 'photo',
    # markov
    'semen_markov', 'razum_markov', 'khashcha_markov', 'bolgov_markov', 'makuha_markov',
    # other
    'auf', 'deadinside', 'call_all'
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


# TODO:fix hentai function
# TODO:[optional, for images] check if file descriptor is closed correctly
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
    with open('data/pacan.txt') as f:
        lines = f.readlines()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=random.choice(lines)
    )


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


# TODO: move photo ids to new config system
async def deadinside(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Я умер, прости
    [name]:deadinside
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    with open('data/deadinside.txt', 'r') as f:
        deadinside_items = list(map(str.strip, f.readlines()))
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=random.choice(deadinside_items)
    )


async def call_all(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Закликати всіх нагору!
    [name]:call_all
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    allowed_users = [1399469085]
    if update.message.from_user.id not in allowed_users:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Вам не дозволено викликати цю команду'
        )
        return None

    with open('data/userids.txt', 'r') as f:
        userids = map(str.strip, f.readlines())
    userstring = ''
    for userid in userids:
        userstring += fr'[\|](tg://user?id={userid})'
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Заклик ФБ14\n'+userstring,
        parse_mode='MarkdownV2'
    )

# TODO: think of a best way to deal with data files
# TODO: refactor function to be more compact and extensible
# TODO: merge some functions (markov)
