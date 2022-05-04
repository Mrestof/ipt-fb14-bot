import random

from telegram import Update
from telegram.ext import CallbackContext

from utils.image import download_wallhaven, remove_wallhaven, resize_image,download_hentai, remove_hentai
from utils.minecraft import server_stats
from utils.markov_chains import markov_sentence


# Meme function to react on Pasha's nickname
def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ну да, хуевый у меня ник.\nНо это блядь не значит '
                                                                    'что на него тыкать нужно!')


# Function to download and send Hentai mangas profile pictures and their tags
def hentai(update: Update, context: CallbackContext) -> None:
    filename = download_hentai()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filename, 'rb'), caption="nhentai-" + filename)
    remove_hentai(filename)


# Function to download and send Erotic photos and their names
def ero(update: Update, context: CallbackContext) -> None:
    if update.message.chat_id == -1001698562626:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Сори в этом чате без эротики, пиши в лс')
    else:
        path = download_wallhaven('ero')
        resize_image(path, 1920)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'), caption=path)
        remove_wallhaven(path)


# Function to download and send Ecchi pictures SFW
def ecchi(update: Update, context: CallbackContext) -> None:
    path = download_wallhaven('ecchi')
    resize_image(path, 1920)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'), caption=path)
    remove_wallhaven(path)


# Function to download and send Photos and their names
def photo(update: Update, context: CallbackContext) -> None:
    path = download_wallhaven('photo')
    resize_image(path, 1920)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'), caption=path)
    remove_wallhaven(path)


# Function to send quotes from real men
def auf(update: Update, context: CallbackContext) -> None:
    with open('data/pacan.txt') as f:
        lines = f.readlines()
    with open('data/pacan.txt') as f:
        lines += f.readlines()
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(lines))


def auf_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/pacan.txt'))


def minecraft(update: Update, context: CallbackContext) -> None:
    #if update.message.chat.type != 'private':
    context.bot.send_message(chat_id=update.effective_chat.id, text=server_stats())


def pavelko_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/artem_pavelko.txt')+' (c) Павелко')


def razum_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/ilya_razum.txt')+' (c) Иля')


def khashcha_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/ivan_khashcha.txt')+' (c) Хаща')


def semen_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/semen_derkach.txt')+' (c) Сэм')


def bolgov_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/kolya_bolgov.txt')+' (c) Коля')


def frolov_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/pasha_frolov.txt')+' (c) Паша')


def makuha_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/andrey_makuha.txt')+' (c) Макуха')


def david_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/david_gavril.txt')+' (c) Давид')


def edward_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/edward_chrome.txt')+' (c) Эд')


def oleg_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/oleg_sergayev.txt')+' (c) Олег')


def deadinside(update: Update, context: CallbackContext) -> None:
    item_number = random.randint(-1, 61)
    if item_number == -1:
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('data/deadinside/Fem.Love-1000-7.mp3', 'rb'))
    elif item_number == 0:
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('data/deadinside/Fem.Love-Zakat.mp3', 'rb'))
    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'data/deadinside/{item_number}.jpg', 'rb'))
# TODO: think of a best way to deal with data files
# TODO: refactor function to be more compact and extensible
