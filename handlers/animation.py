from telegram import Update
from telegram.ext import CallbackContext


def animation_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    elif update.message.chat.type == 'private':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Chat functions only for groups')
