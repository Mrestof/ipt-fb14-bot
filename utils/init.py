# TODO: merge separate methods into one class where makes sense
from typing import Callable
from dataclasses import dataclass

from telegram import Bot, BotCommand, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext

from handlers.text import text_messages
import handlers.command as command
from handlers.photo import photo_messages
from handlers.video import video_messages
from handlers.audio import audio_messages
from handlers.animation import animation_messages
from handlers.video_note import video_note_messages
from handlers.voice import voice_messages
from handlers.sticker import sticker_messages


@dataclass
class CommandAttrs:
    description: str
    name: str
    is_hidden: bool


def _get_command_attrs(command: Callable[[Update, CallbackContext], None]) -> CommandAttrs:
    # TODO: try to beautify this
    data = command.__doc__.splitlines()
    name, description, is_hidden = '', '', True
    for line in data:
        if line.strip().startswith('[name]'):
            name = line.split(':')[1].strip()
        if line.strip().startswith('[description]'):
            description = line.split(':')[1].strip()
        if line.strip().startswith('[is_hidden]'):
            is_hidden_raw = line.split(':')[1].strip()
            if is_hidden_raw == 'False':
                is_hidden = False
            elif is_hidden_raw == 'True':
                is_hidden = True
            else:
                raise SystemExit(f'error in docstring for {command.__name__} command')
    return CommandAttrs(description, name, is_hidden)


# Function to get token from file
def get_token() -> str:
    with open('data/token.txt', 'r') as f:
        token = f.readline().strip()
    return token


# Function to set commands description
def set_commands(token: str) -> None:
    commands = []
    for cmd_name in command.__all__:
        cmd_func = getattr(command, cmd_name)
        cmd_attrs = _get_command_attrs(cmd_func)
        if cmd_attrs.is_hidden:
            continue
        bot_command = BotCommand(cmd_attrs.name, cmd_attrs.description)
        commands.append(bot_command)
    bot = Bot(token)
    bot.set_my_commands(commands)


# Function to declare all commands handlers for bot (Telegram API)
def get_updater(token: str) -> Updater:
    # TODO: make the following code more compact (with the help of for cycle)
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # text handlers
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

    # command handlers
    for cmd_name in command.__all__:
        cmd_func = getattr(command, cmd_name)
        cmd_custom_name = _get_command_attrs(cmd_func).name
        cmd_handler = CommandHandler(cmd_custom_name, cmd_func)
        dispatcher.add_handler(cmd_handler)

    return updater
