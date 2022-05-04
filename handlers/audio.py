from telegram import Update
from telegram.ext import CallbackContext

from utils.logging import chat_logging_audio

with open('data/loggedgroups.txt', 'r') as f:
    loggedgroups = [int(i.strip()) for i in f.readlines()]


def audio_messages(update: Update, context: CallbackContext) -> None:
    if update.message.chat.id in loggedgroups:
        chat_logging_audio(update)
    # context.bot.send_audio(chat_id=update.effective_chat.id, audio=update.message.audio.file_id)
