from telegram import Bot, BotCommand
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

from handlers.text import text_messages
from handlers.command import pasha_nick, makuha_markov, mute_makuha, unmute_makuha
from handlers.photo import photo_messages
from handlers.video import video_messages
from handlers.audio import audio_messages
from handlers.animation import animation_messages
from handlers.video_note import video_note_messages
from handlers.voice import voice_messages
from handlers.sticker import sticker_messages


def get_token() -> str:
    with open('data/token.txt', 'r') as f:
        token = f.readline().strip()
    return token


def set_commands(token: str) -> None:
    # TODO: take the names and descriptions of the commands from codebase
    commands = [
        BotCommand('mute_makuha', 'Мут Негра'),
        BotCommand('unmute_makuha', 'Анмут Негра'),
        BotCommand('makuha_markov', 'Запасний Негр'),
    ]
    bot = Bot(token)
    bot.set_my_commands(commands)


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

    video_note_handler = MessageHandler(Filters.video_note & (~Filters.command), video_note_messages)
    dispatcher.add_handler(video_note_handler)

    audio_handler = MessageHandler(Filters.audio & (~Filters.command), audio_messages)
    dispatcher.add_handler(audio_handler)

    voice_handler = MessageHandler(Filters.voice & (~Filters.command), voice_messages)
    dispatcher.add_handler(voice_handler)

    animation_handler = MessageHandler(Filters.animation & (~Filters.command), animation_messages)
    dispatcher.add_handler(animation_handler)

    sticker_handler = MessageHandler(Filters.animation & (~Filters.command), sticker_messages)
    dispatcher.add_handler(sticker_handler)

    mute_makuha_handler = CommandHandler('mute_makuha', mute_makuha)
    dispatcher.add_handler(mute_makuha_handler)

    unmute_makuha_handler = CommandHandler('unmute_makuha', unmute_makuha)
    dispatcher.add_handler(unmute_makuha_handler)

    makuha_markov_handler = CommandHandler('makuha_markov', makuha_markov)
    dispatcher.add_handler(makuha_markov_handler)

    pasha_nick_handler = CommandHandler('I3700ch3g0', pasha_nick)
    dispatcher.add_handler(pasha_nick_handler)

    return updater
