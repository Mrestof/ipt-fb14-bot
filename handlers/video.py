from telegram import Update
from telegram.ext import CallbackContext
from random import choice, randint
from utils.readfile import get_makuha_paste


def video_messages(update: Update, context: CallbackContext) -> None:
    animations = ['CgACAgIAAx0CaaeLPAACBBVikRB4awKvVaMsue44-iifMYJT8AACuhUAAvJk4EkraQAB9APB8Z8kBA',
                  'CgACAgIAAx0CaaeLPAACBBZikRB5DEIhMvbuNNJ_3-TdmmdJ-wACuBcAAsV-cUt77ujvfNHsnSQE']
    if update.edited_message is not None:
        return None
    if update.message.from_user.id == 658890395:
        if randint(0, 9) == 0:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=get_makuha_paste(),
                                     reply_to_message_id=update.message.message_id)
        else:
            context.bot.send_animation(chat_id=update.effective_chat.id,
                                       animation=choice(animations),
                                       reply_to_message_id=update.message.message_id)
