from telegram import Update
from telegram.ext import CallbackContext

from utils.logging import chat_logging_video

with open('data/loggedgroups.txt', 'r') as f:
    loggedgroups = [int(i.strip()) for i in f.readlines()]


def video_messages(update: Update, context: CallbackContext) -> None:
    if update.message.chat.id in loggedgroups:
        chat_logging_video(update)
    # context.bot.send_video(chat_id=update.effective_chat.id, video=update.message.video.file_id)
