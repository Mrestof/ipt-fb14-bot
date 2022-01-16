import random

from telegram import Update
from telegram.ext import CallbackContext

from utils.nhentai import download_hentai, remove_hentai
from utils.wallhaven import download_wallhaven, remove_wallhaven


# Meme function to react on Pasha's nickname
def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ну да, хуевый у меня ник.\nНо это блядь не значит '
                                                                    'что на него тыкать нужно!')


# Function to download and send Hentai mangas profile pictures and their tags
def hentai(update: Update, context: CallbackContext) -> None:
    filename = download_hentai()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filename, 'rb'), caption="nhentai-" + filename)
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    remove_hentai(filename)


# Function to download and send Ecchi pictures SFW
def ecchi(update: Update, context: CallbackContext) -> None:
    filename = download_wallhaven('ecchi')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filename, 'rb'), caption=filename)
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    remove_wallhaven(filename)


# Function to download and send Erotic photos and their names
def ero(update: Update, context: CallbackContext) -> None:
    filename = download_wallhaven('ero')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filename, 'rb'), caption=filename)
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    remove_wallhaven(filename)


# Function to download and send Photos and their names
def photo(update: Update, context: CallbackContext) -> None:
    filename = download_wallhaven('photo')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filename, 'rb'), caption=filename)
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    remove_wallhaven(filename)


# Function to send quotes from real men
def auf(update: Update, context: CallbackContext) -> None:
    with open("data/pacanskie-citaty-pro-zhizn") as f:
        lines = f.readlines()
    context.bot.send_message(chat_id=update.effective_chat.id, text=lines[random.randint(0, 100)])
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)


# Other variants of saving messages
'''
def important_data_write(update: Update, context: CallbackContext) -> None:
    reply_text = update.message.reply_to_message.text
    tg_user = update.message.reply_to_message.from_user


def important_data_read(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='1')
    print(1)
'''
