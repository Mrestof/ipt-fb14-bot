from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

from handlers.text import text_messages
from handlers.commands import hentai, pasha_nick, important_data_read, important_data_write


def get_token() -> str:
    with open('data/token.txt', 'r') as f:
        token = f.readline().strip()
    return token


def get_updater(token: str) -> Updater:
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    important_data_write_handler = CommandHandler('save', important_data_write)
    dispatcher.add_handler(important_data_write_handler)

    important_data_read_handler = CommandHandler('read', important_data_read)
    dispatcher.add_handler(important_data_read_handler)

    pasha_nick_handler = CommandHandler('I3700ch1u', pasha_nick)
    dispatcher.add_handler(pasha_nick_handler)

    hentai_handler = CommandHandler('hentai', hentai)
    dispatcher.add_handler(hentai_handler)

    text_handler = MessageHandler(Filters.text & (~Filters.command), text_messages)
    dispatcher.add_handler(text_handler)

    return updater
