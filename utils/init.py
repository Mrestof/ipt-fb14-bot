import datetime
from typing import Callable, NamedTuple

from telegram import BotCommand, Update
from telegram.ext import MessageHandler, filters, CommandHandler, CallbackContext, ApplicationBuilder, Application

from handlers.animation import animation_messages
from handlers.audio import audio_messages
import handlers.command as command
from handlers.jobs import birthday_check, update_schedule, diary_remove_day, diary_remind
from handlers.photo import photo_messages
from handlers.sticker import sticker_messages
from handlers.text import text_messages
from handlers.video import video_messages
from handlers.video_note import video_note_messages
from handlers.voice import voice_messages
from utils.log import get_logger

logger = get_logger(__name__)


class CommandAttrs(NamedTuple):
    name: str
    description: str
    is_hidden: bool


def _get_command_attrs(cmd: Callable[[Update, CallbackContext], None]) -> CommandAttrs:
    cmd_name = cmd.__name__
    try:
        assert cmd.__doc__ is not None
    except AssertionError:
        logger.critical('error: %r command does not have a docstring', cmd_name)
        raise SystemExit(1)
    data = cmd.__doc__.splitlines()
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
                logger.critical(
                    'syntax of docstring for %r command is wrong'
                    ' in [is_hidden] section',
                    cmd_name
                )
                raise SystemExit(1)
    cmd_attrs = CommandAttrs(name, description, is_hidden)
    logger.debug('%(cn)s: %(ca)s', {'cn': cmd_name, 'ca': cmd_attrs})
    return cmd_attrs


# Function to get token from file
def get_token() -> str:
    try:
        with open('data/token.txt', 'r') as f:
            token = f.readline().strip()
        logger.info('got token from file: %s', token)
        return token
    except FileNotFoundError as e:
        logger.critical('token must be specified in the %r file', e.filename)
        raise SystemExit(1)


# Function to set commands description
async def set_commands(application: Application) -> None:
    commands = []
    for cmd_name in command.__all__:
        cmd_func = getattr(command, cmd_name)
        cmd_attrs = _get_command_attrs(cmd_func)
        if cmd_attrs.is_hidden:
            continue
        bot_command = BotCommand(cmd_attrs.name, cmd_attrs.description)
        commands.append(bot_command)
    await application.bot.set_my_commands(commands)
    logger.debug('set all bot commands')


# Function to declare all commands handlers for bot (Telegram API)
def get_application(token: str) -> Application:
    application = (
        ApplicationBuilder()
        .token(token)
        .post_init(set_commands)
        .build()
    )
    logger.debug('build the application')

    # message handlers
    text_handlers = {
        animation_messages: filters.ANIMATION,
        audio_messages: filters.AUDIO,
        photo_messages: filters.PHOTO,
        sticker_messages: filters.Sticker.ALL,
        text_messages: filters.TEXT,
        video_messages: filters.VIDEO,
        video_note_messages: filters.VIDEO_NOTE,
        voice_messages: filters.VOICE,
    }
    for key, var in text_handlers.items():
        application.add_handler(MessageHandler(var & (~filters.COMMAND), key))
    logger.debug('set all bot text handlers')

    # command handlers
    for cmd_name in command.__all__:
        cmd_func = getattr(command, cmd_name)
        cmd_custom_name = _get_command_attrs(cmd_func).name
        cmd_handler = CommandHandler(cmd_custom_name, cmd_func)
        application.add_handler(cmd_handler)
    logger.debug('set all bot command handlers')

    job_queue = application.job_queue
    try:
        assert job_queue is not None
    except AssertionError:
        logger.critical('PTB is installed without job-queue')
        raise SystemExit(1)

    job_queue.run_daily(birthday_check, time=datetime.time(hour=10, minute=0))  # UTC timezone
    job_queue.run_daily(diary_remind, time=datetime.time(hour=10, minute=0))  # UTC timezone
    job_queue.run_daily(diary_remove_day, time=datetime.time(hour=0, minute=0))  # UTC timezone
    job_queue.run_daily(update_schedule, time=datetime.time(hour=0, minute=0))
    logger.debug('set all bot jobs')

    return application
