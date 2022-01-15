import random

from telegram import Update
from telegram.ext import CallbackContext

from utils.hentai import download_hentai, remove_hentai


def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ну да, хуевый у меня ник.\nНо это блядь не значит '
                                                                    'что на него тыкать нужно!')


def hentai(update: Update, context: CallbackContext) -> None:
    filename = download_hentai()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filename, 'rb'), caption=filename)
    remove_hentai(filename)


def auf(update: Update, context: CallbackContext) -> None:
    with open("data/pacanskie-citaty-pro-zhizn") as f:
        lines = f.readlines()
    context.bot.send_message(chat_id=update.effective_chat.id, text=lines[random.randint(0,100)])


def important_data_write(update: Update, context: CallbackContext) -> None:
    reply_text = update.message.reply_to_message.text
    tg_user = update.message.reply_to_message.from_user


def important_data_read(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='1')
    print(1)

