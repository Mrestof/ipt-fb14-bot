from telegram import Update
from telegram.ext import CallbackContext
from utils.get_time import get_time


def photo_messages(update: Update, context: CallbackContext) -> None:
    if update.message.chat.type == 'private' and update.message.from_user.id == 483029014:
        # photo ids for future optimiztion (Сори Саня, это нужно будет)
        print(get_time(), update.message.photo[0].file_id)
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo=update.message.photo[0].file_id)
