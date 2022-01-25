import random

from telegram import Update
from telegram.ext import CallbackContext

from utils.nhentai import download_hentai, remove_hentai
from utils.wallhaven import download_wallhaven, remove_wallhaven
from utils.resize_image import resize_image
from utils.minecraft import server_stats


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


# Function to download and send Erotic photos and their names
def ero(update: Update, context: CallbackContext) -> None:
    if update.message.chat_id == -1001698562626:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Сори в этом чате без эротики, пиши в лс')
    else:
        path = download_wallhaven('ero')
        resize_image(path, 1920)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'), caption=path)
        # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
        remove_wallhaven(path)


# Function to download and send Ecchi pictures SFW
def ecchi(update: Update, context: CallbackContext) -> None:
    path = download_wallhaven('ecchi')
    resize_image(path, 1920)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'), caption=path)
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    remove_wallhaven(path)


# Function to download and send Photos and their names
def photo(update: Update, context: CallbackContext) -> None:
    path = download_wallhaven('photo')
    resize_image(path, 1920)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'), caption=path)
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    remove_wallhaven(path)


# Function to send quotes from real men
def auf(update: Update, context: CallbackContext) -> None:
    with open("data/pacanskie-citaty-pro-zhizn") as f:
        lines = f.readlines()
    context.bot.send_message(chat_id=update.effective_chat.id, text=lines[random.randint(0, 252)])
    # context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)


def anekdot(update: Update, context: CallbackContext) -> None:
    with open('data/anekdots.txt') as f:
        a = ''.join([f.readline() for _ in range(5056)]).split('###')
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(a))


def minecraft(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=server_stats())
