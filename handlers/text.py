from telegram import Update
from telegram.ext import CallbackContext


def text_messages(update: Update, context: CallbackContext) -> None:
    if update.edited_message is not None:
        return None
    tg_message = update.message.text
    tg_user = update.message.from_user

    with open('data/users_messages/' + str(tg_user.id), 'a') as userf:
        userf.write(tg_message + '\n')

    if 'виконати наказ 66' in tg_message.lower() and tg_user.id == 483029014:
        context.bot.leaveChat(chat_id=update.effective_chat.id)
        return None

    # TODO: make two functions for fucking makuha
