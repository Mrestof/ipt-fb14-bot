from telegram import Update
from telegram.ext import CallbackContext


async def audio_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    else:
        pass
