from telegram import Update
from telegram.ext import CallbackContext


def audio_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    else:
        pass
    # context.bot.send_audio(chat_id=update.effective_chat.id, audio=update.message.audio.file_id)
