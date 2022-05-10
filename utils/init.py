from telegram import Bot, BotCommand
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

from handlers.text import text_messages
from handlers.commands import hentai, pasha_nick, auf, ero, ecchi, photo, minecraft, deadinside, auf_markov,\
    pavelko_markov, razum_markov, khashcha_markov, bolgov_markov, semen_markov, frolov_markov, makuha_markov, \
    david_markov, edward_markov, oleg_markov
from handlers.image import photo_messages
from handlers.video import video_messages
from handlers.audio import audio_messages
from handlers.animation import animation_messages
from handlers.jobs import alive_minute_job, kill_jobs

# Function to get token from file
def get_token() -> str:
    with open('data/token.txt', 'r') as f:
        token = f.readline().strip()
    return token


# Function to set commands description
def set_commands(token: str) -> None:
    # TODO: take the names and descriptions of the commands from codebase
    commands = [BotCommand('hentai', 'Відійти на 5 хвилин'),
                BotCommand('ecchi', 'Safe for батьки'),
                BotCommand('ero', 'Шкіряні мішки з м`ясом'),
                BotCommand('auf', 'АУФ'),
                BotCommand('photo', 'Вах яка краса'),
                BotCommand('deadinside', 'Я умер, прости'),
                BotCommand('minecraft', 'Ваня досить ферми будувати'),
                BotCommand('pavelko_markov', 'Запасний Артем Павелко'),
                BotCommand('razum_markov', 'Запасний Іля Разум'),
                BotCommand('khashcha_markov', 'Запасний Бір'),
                BotCommand('semen_markov', 'Запасна ввічливість.'),
                BotCommand('bolgov_markov', 'Запасний Коля'),
                BotCommand('frolov_markov', 'Запасний Паша'),
                BotCommand('makuha_markov', 'Запасний Негр'),
                BotCommand('david_markov', 'Запасний Давід'),
                BotCommand('edward_markov', 'Запасний Хром'),
                BotCommand('oleg_markov', 'Запасний Олег')
                ]
    bot = Bot(token)
    bot.set_my_commands(commands)


# Function to declare all commands handlers for bot (Telegram API)
def get_updater(token: str) -> Updater:
    # TODO: make the following code more compact (with the help of for cycle)
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    alive_minute_handler = CommandHandler('test', alive_minute_job)
    updater.dispatcher.add_handler(alive_minute_handler)

    kill_jobs_handler = CommandHandler('kill', kill_jobs)
    updater.dispatcher.add_handler(kill_jobs_handler)

    text_handler = MessageHandler(Filters.text & (~Filters.command), text_messages)
    dispatcher.add_handler(text_handler)

    photo_handler = MessageHandler(Filters.photo & (~Filters.command), photo_messages)
    dispatcher.add_handler(photo_handler)

    video_handler = MessageHandler(Filters.video & (~Filters.command), video_messages)
    dispatcher.add_handler(video_handler)

    audio_handler = MessageHandler(Filters.audio & (~Filters.command), audio_messages)
    dispatcher.add_handler(audio_handler)

    animation_handler = MessageHandler(Filters.animation & (~Filters.command), animation_messages)
    dispatcher.add_handler(animation_handler)

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

    minecraft_handler = CommandHandler('minecraft', minecraft)
    dispatcher.add_handler(minecraft_handler)

    deadinside_handler = CommandHandler('deadinside', deadinside)
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
