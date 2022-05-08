from telegram import Update
from telegram.ext import CallbackContext


def video_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    else:
        pass
    # context.bot.send_video(chat_id=update.effective_chat.id, video=update.message.video.file_id)
