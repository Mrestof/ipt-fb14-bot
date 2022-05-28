from telegram import Update
from telegram.ext import CallbackContext
from random import choice


def video_note_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    kiva_reply = ['Москаляку на гілляку', 'Бан нахуй', 'Вийди з чату', 'Кива пидор ипанный (c) Макуха']
    if update.message.forward_from_chat is not None:
        if update.message.forward_from_chat.id == -1001235238484:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=choice(kiva_reply),
                                     reply_to_message_id=update.message.message_id)
