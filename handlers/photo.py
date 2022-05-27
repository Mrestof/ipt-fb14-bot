from telegram import Update
from telegram.ext import CallbackContext
from random import randint, choice
from utils.readfile import get_makuha_paste


def photo_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    elif update.message.chat.type == 'private' and update.message.from_user.id == 483029014:
        # photo ids for future optimiztion (Сори Саня, это нужно будет)
        print(update.message.photo[0].file_id)
    animations = ['CgACAgIAAx0CaaeLPAACBBVikRB4awKvVaMsue44-iifMYJT8AACuhUAAvJk4EkraQAB9APB8Z8kBA',
                  'CgACAgIAAx0CaaeLPAACBBZikRB5DEIhMvbuNNJ_3-TdmmdJ-wACuBcAAsV-cUt77ujvfNHsnSQE']
    if update.message.from_user.id == 658890395:
        if randint(0, 9) == 0:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=get_makuha_paste(),
                                     reply_to_message_id=update.message.message_id)
        else:
            context.bot.send_animation(chat_id=update.effective_chat.id,
                                       animation=choice(animations),
                                       reply_to_message_id=update.message.message_id)
