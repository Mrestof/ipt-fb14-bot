import random

from telegram import Update
from telegram.ext import CallbackContext

from utils.image import download_wallhaven, remove_wallhaven, resize_image, download_hentai, remove_hentai
from utils.minecraft import server_stats
from utils.markov_chains import markov_sentence


__all__ = [
    # hidden
    'ping', 'pasha_nick',
    # image
    'hentai', 'ero', 'ecchi', 'photo',
    # markov
    'pavelko_markov', 'razum_markov', 'khashcha_markov', 'bolgov_markov', 'makuha_markov', 'auf_markov',
    # other
    'auf', 'minecraft', 'deadinside',
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text='pong')


async def pasha_nick(update: Update, context: CallbackContext) -> None:
    """Meme function to react on Pasha's nickname.

    [description]:
    [name]:I3700ch3g0
    [is_hidden]:True

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='Ну тай, хуйовий в мене нік.\nАле це бляха не значить що на нього тикати потрібно!')


async def hentai(update: Update, context: CallbackContext) -> None:
    """Function to download and send Hentai mangas profile pictures and their tags.

    [description]:Відійти на 5 хвилин
    [name]:hentai
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    filename = download_hentai()
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(filename, 'rb'),
                                 caption="nhentai-" + filename)
    remove_hentai(filename)


async def ero(update: Update, context: CallbackContext) -> None:
    """Function to download and send Erotic photos and their names

    [description]:Шкіряні мішки з м`ясом
    [name]:ero
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    if update.message.chat_id == -1001698562626:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='Вибач, у цьому чаті без еротики')
    else:
        path = download_wallhaven('ero')
        resize_image(path, 1920)
        await context.bot.send_photo(chat_id=update.effective_chat.id,
                                     photo=open(path, 'rb'),
                                     caption=path)
        remove_wallhaven(path)


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
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(path, 'rb'),
                                 caption=path)
    remove_wallhaven(path)


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
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(path, 'rb'),
                                 caption=path)
    remove_wallhaven(path)


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
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=random.choice(lines))


async def auf_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:
    [name]:auf_markov
    [is_hidden]:True

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=markov_sentence('data/pacan.txt'))


async def minecraft(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Ваня досить ферми будувати
    [name]:minecraft
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    # if update.message.chat.type != 'private':
    await context.bot.send_message(chat_id=update.effective_chat.id, text=server_stats())


async def pavelko_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Артем Павелко
    [name]:pavelko_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=markov_sentence('data/users_messages/890603480') + ' (c) Павелко')


async def razum_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Іля Разум
    [name]:razum_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=markov_sentence('data/users_messages/588535976') + ' (c) Иля')


async def khashcha_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Бір
    [name]:khashcha_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=markov_sentence('data/users_messages/1472956766') + ' (c) Хаща')


async def bolgov_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Коля
    [name]:bolgov_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=markov_sentence('data/users_messages/619857691') + ' (c) Коля')


async def makuha_markov(update: Update, context: CallbackContext) -> None:
    """...

    [description]:Запасний Негр
    [name]:makuha_markov
    [is_hidden]:False

    :param update:
    :param context:
    :return:
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=markov_sentence('data/users_messages/658890395') + ' (c) Макуха')


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
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=random.choice(deadinside_items))
# TODO: think of a best way to deal with data files
# TODO: refactor function to be more compact and extensible
