from telegram import Update
from telegram.ext import CallbackContext


def photo_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    elif update.message.chat.type == 'private' and update.message.from_user.id == 483029014:
        # photo ids for future optimiztion (Сори Саня, это нужно будет)
        print(update.message.photo[0].file_id)
