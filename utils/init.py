from telegram import Bot, BotCommand
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

from handlers.text import text_messages
from handlers.commands import hentai, pasha_nick, auf, ero, ecchi, photo  # , important_data_read, important_data_write


def get_token() -> str:
    with open('data/token.txt', 'r') as f:
        token = f.readline().strip()
    return token


def set_commands(token: str) -> None:
    commands = [BotCommand('hentai', 'Отойти на 5 минут'),
                BotCommand('ecchi', 'Safe for родители'),
                BotCommand('ero', 'Кожаные мешки с мясом'),
                BotCommand('auf', 'АУФ'),
                BotCommand('photo', 'Вах какая красота')]
    bot = Bot(token)
    bot.set_my_commands(commands)


def get_updater(token: str) -> Updater:
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    text_handler = MessageHandler(Filters.text & (~Filters.command), text_messages)
    dispatcher.add_handler(text_handler)

    pasha_nick_handler = CommandHandler('I3700ch1u', pasha_nick)
    dispatcher.add_handler(pasha_nick_handler)

    hentai_handler = CommandHandler('hentai', hentai)
    dispatcher.add_handler(hentai_handler)

    ero_handler = CommandHandler('ero', ero)
    dispatcher.add_handler(ero_handler)

    ecchi_handler = CommandHandler('ecchi', ecchi)
    dispatcher.add_handler(ecchi_handler)

    photo_handler = CommandHandler('photo', photo)
    dispatcher.add_handler(photo_handler)

    auf_handler = CommandHandler('auf', auf)
    dispatcher.add_handler(auf_handler)

    return updater


'''
    important_data_write_handler = CommandHandler('save', important_data_write)
    dispatcher.add_handler(important_data_write_handler)

    important_data_read_handler = CommandHandler('read', important_data_read)
    dispatcher.add_handler(important_data_read_handler)'''
