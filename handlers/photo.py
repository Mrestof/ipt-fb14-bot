from telegram import Update
from telegram.ext import CallbackContext

from utils.get_time import get_time
from utils.logging import chat_logging_photo

with open('data/loggedgroups.txt', 'r') as f:
    loggedgroups = [int(i.strip()) for i in f.readlines()]


def photo_messages(update: Update, context: CallbackContext) -> None:
    if update.message.chat.id in loggedgroups:
        chat_logging_photo(update)
    if update.message.chat.type == 'private' and update.message.from_user.id == 483029014:
        # photo ids for future optimiztion (Сори Саня, это нужно будет)
        print(get_time(), update.message.photo[0].file_id)
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo=update.message.photo[0].file_id)
