from telegram import Update
from telegram.ext import CallbackContext
from random import choice


def video_note_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    else:
        pass
