# TODO: merge separate methods into one class where makes sense
from typing import Callable
from dataclasses import dataclass

from telegram import Bot, BotCommand, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext

from handlers.animation import animation_messages
from handlers.audio import audio_messages
import handlers.command as command
from handlers.jobs import pavelko_notify
from handlers.photo import photo_messages
from handlers.sticker import sticker_messages
from handlers.text import text_messages
from handlers.video import video_messages
from handlers.video_note import video_note_messages
from handlers.voice import voice_messages


@dataclass
class CommandAttrs:
    description: str
    name: str
    is_hidden: bool


def _get_command_attrs(command: Callable[[Update, CallbackContext], None]) -> CommandAttrs:
    # TODO: refactor this to be more readable and less error prone
    try:
        data = command.__doc__.splitlines()
    except AttributeError:
        raise SystemExit(f'error: {command.__name__:r} command does not have a docstring')
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
                raise SystemExit(f'error: syntax of docstring for {command.__name__:r} command is wrong '
                                 ' in [is_hidden] section')
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

    # message handlers
    text_handlers = {animation_messages: Filters.animation,
                     audio_messages: Filters.audio,
                     photo_messages: Filters.photo,
                     sticker_messages: Filters.sticker,
                     text_messages: Filters.text,
                     video_messages: Filters.video,
                     video_note_messages: Filters.video_note,
                     voice_messages: Filters.voice,
                     }
    for key, var in text_handlers.items():
        dispatcher.add_handler(MessageHandler(var & (~Filters.command), key))

    # command handlers
    for cmd_name in command.__all__:
        cmd_func = getattr(command, cmd_name)
        cmd_custom_name = _get_command_attrs(cmd_func).name
        cmd_handler = CommandHandler(cmd_custom_name, cmd_func)
        dispatcher.add_handler(cmd_handler)

    job_queue = updater.job_queue
    job_queue.run_repeating(pavelko_notify, interval=10.0, first=0.0)

    return updater
