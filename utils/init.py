from telegram import Bot, BotCommand
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

from handlers.text import text_messages
from handlers.commands import hentai, pasha_nick, auf, anekdot, ero, ecchi, photo, minecraft, deadinside, auf_markov,\
    pavelko_markov, razum_markov, khashcha_markov, bolgov_markov, semen_markov, frolov_markov, makuha_markov, \
    david_markov, edward_markov, oleg_markov
from handlers.photo import photo_messages
from handlers.video import video_messages
from handlers.audio import audio_messages


# Function to get token from file
def get_token() -> str:
    with open('data/token.txt', 'r') as f:
        token = f.readline().strip()
    return token


# Function to set commands description
def set_commands(token: str) -> None:
    # TODO: take the names and descriptions of the commands from codebase
    commands = [BotCommand('hentai', 'Отойти на 5 минут'),
                BotCommand('ecchi', 'Safe for родители'),
                BotCommand('ero', 'Кожаные мешки с мясом'),
                BotCommand('anekdot', 'Помереть со смеху'),
                BotCommand('auf', 'АУФ'),
                BotCommand('photo', 'Вах какая красота'),
                BotCommand('1000minus7', 'Я умер, прости'),
                BotCommand('minecraft', 'Ваня хватит фермы строить'),
                BotCommand('pavelko_markov', 'Запасной Артем Павелко'),
                BotCommand('razum_markov', 'Запасной Иля Разум'),
                BotCommand('khashcha_markov', 'Запасная Тайга'),
                BotCommand('semen_markov', 'Запасная Вежливость'),
                BotCommand('bolgov_markov', 'Запасной Коля'),
                BotCommand('frolov_markov', 'Запасной Паша'),
                BotCommand('makuha_markov', 'Запасной Негр'),
                BotCommand('david_markov', 'Запасной Давид'),
                BotCommand('edward_markov', 'Запасной Хром'),
                BotCommand('oleg_markov', 'Запасной Олег')
                ]
    bot = Bot(token)
    bot.set_my_commands(commands)


# Function to declare all commands handlers for bot (Telegram API)
def get_updater(token: str) -> Updater:
    # TODO: make the following code more compact (with the help of for cycle)
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    text_handler = MessageHandler(Filters.text & (~Filters.command), text_messages)
    dispatcher.add_handler(text_handler)

    photo_handler = MessageHandler(Filters.photo & (~Filters.command), photo_messages)
    dispatcher.add_handler(photo_handler)

    video_handler = MessageHandler(Filters.video & (~Filters.command), video_messages)
    dispatcher.add_handler(video_handler)

    audio_handler = MessageHandler(Filters.audio, audio_messages)
    dispatcher.add_handler(audio_handler)

    pasha_nick_handler = CommandHandler('I3700ch3g0', pasha_nick)
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

    auf_markov_handler = CommandHandler('auf_markov', auf_markov)
    dispatcher.add_handler(auf_markov_handler)

    anekdot_handler = CommandHandler('anekdot', anekdot)
    dispatcher.add_handler(anekdot_handler)

    minecraft_handler = CommandHandler('minecraft', minecraft)
    dispatcher.add_handler(minecraft_handler)

    deadinside_handler = CommandHandler('1000minus7', deadinside)
    dispatcher.add_handler(deadinside_handler)

    pavelko_markov_handler = CommandHandler('pavelko_markov', pavelko_markov)
    dispatcher.add_handler(pavelko_markov_handler)

    razum_markov_handler = CommandHandler('razum_markov', razum_markov)
    dispatcher.add_handler(razum_markov_handler)

    khashcha_markov_handler = CommandHandler('khashcha_markov', khashcha_markov)
    dispatcher.add_handler(khashcha_markov_handler)

    semen_markov_handler = CommandHandler('semen_markov', semen_markov)
    dispatcher.add_handler(semen_markov_handler)

    bolgov_markov_handler = CommandHandler('bolgov_markov', bolgov_markov)
    dispatcher.add_handler(bolgov_markov_handler)

    frolov_markov_handler = CommandHandler('frolov_markov', frolov_markov)
    dispatcher.add_handler(frolov_markov_handler)

    makuha_markov_handler = CommandHandler('makuha_markov', makuha_markov)
    dispatcher.add_handler(makuha_markov_handler)

    david_markov_handler = CommandHandler('david_markov', david_markov)
    dispatcher.add_handler(david_markov_handler)

    edward_markov_handler = CommandHandler('edward_markov', edward_markov)
    dispatcher.add_handler(edward_markov_handler)

    oleg_markov_handler = CommandHandler('oleg_markov', oleg_markov)
    dispatcher.add_handler(oleg_markov_handler)

    return updater
