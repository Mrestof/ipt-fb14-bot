import datetime

from telegram import Update
from telegram.ext import CallbackContext
from random import choice

def photo_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    elif update.message.chat.type == 'private' and update.message.from_user.id == 483029014:
        # photo ids for future optimiztion (Сори Саня, это нужно будет)
        print(datetime.datetime.now(), update.message.photo[0].file_id)
    kiva_reply = ['Москаляку на гілляку', 'Бан нахуй', 'Вийди з чату', 'Кива пидор ипанный (c) Макуха']
    if update.message.forward_from_chat is not None:
        if update.message.forward_from_chat.id == -1001235238484:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=choice(kiva_reply),
                                     reply_to_message_id=update.message.message_id)
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo=update.message.photo[0].file_id)
