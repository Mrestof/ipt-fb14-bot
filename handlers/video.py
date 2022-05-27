from telegram import Update
from telegram.ext import CallbackContext
from random import choice, randint

with open('data/makuha_paste.txt') as f:
    makuha_paste = f.readline()


def video_messages(update: Update, context: CallbackContext) -> None:
    animations = ['CgACAgIAAx0CaaeLPAACAX5iej9dr5dUvB2JeURycM_S8oNLpQACuhUAAvJk4ElOKlGmLnon9CQE',
                  'CgACAgIAAx0CaaeLPAACAXliej8ngzRcN7H-qmYoi-245HejRQACuBcAAsV-cUu9fQToemL9HSQE']
    if update.edited_message is not None:
        return None
    if update.message.from_user.id == 658890395:
        if randint(0, 1):
            context.bot.send_animation(chat_id=update.effective_chat.id,
                                       animation=choice(animations),
                                       reply_to_message_id=update.message.message_id)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=makuha_paste,
                                     reply_to_message_id=update.message.message_id)
