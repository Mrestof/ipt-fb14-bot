import random

from telegram import Update
from telegram.ext import CallbackContext

from utils.image import download_wallhaven, remove_wallhaven, resize_image, download_hentai, remove_hentai
from utils.minecraft import server_stats
from utils.markov_chains import markov_sentence


# Meme function to react on Pasha's nickname
def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Ну тай, хуйовий в мене нік.\nАле це бляха не значить що на нього тикати потрібно!')


# Function to download and send Hentai mangas profile pictures and their tags
def hentai(update: Update, context: CallbackContext) -> None:
    filename = download_hentai()
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(filename, 'rb'),
                           caption="nhentai-" + filename)
    remove_hentai(filename)


# Function to download and send Erotic photos and their names
def ero(update: Update, context: CallbackContext) -> None:
    if update.message.chat_id == -1001698562626:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Вибач, у цьому чаті без еротики')
    else:
        path = download_wallhaven('ero')
        resize_image(path, 1920)
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open(path, 'rb'),
                               caption=path)
        remove_wallhaven(path)


# Function to download and send Ecchi pictures SFW
def ecchi(update: Update, context: CallbackContext) -> None:
    path = download_wallhaven('ecchi')
    resize_image(path, 1920)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(path, 'rb'),
                           caption=path)
    remove_wallhaven(path)


# Function to download and send Photos and their names
def photo(update: Update, context: CallbackContext) -> None:
    path = download_wallhaven('photo')
    resize_image(path, 1920)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(path, 'rb'),
                           caption=path)
    remove_wallhaven(path)


# Function to send quotes from real men
def auf(update: Update, context: CallbackContext) -> None:
    with open('data/pacan.txt') as f:
        lines = f.readlines()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=random.choice(lines))


def auf_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/pacan.txt'))


def minecraft(update: Update, context: CallbackContext) -> None:
    # if update.message.chat.type != 'private':
    context.bot.send_message(chat_id=update.effective_chat.id, text=server_stats())


def pavelko_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/890603480') + ' (c) Павелко')


def razum_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/588535976') + ' (c) Иля')


def khashcha_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/1472956766') + ' (c) Хаща')


def semen_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/1399469085') + ' (c) Сэм')


def bolgov_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/619857691') + ' (c) Коля')


def frolov_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/483029014') + ' (c) Паша')


def makuha_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/658890395') + ' (c) Макуха')


def david_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/559443434') + ' (c) Давид')


def edward_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/393560656') + ' (c) Эд')


def oleg_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/367146646') + ' (c) Олег')


def deadinside(update: Update, context: CallbackContext) -> None:
    with open('data/deadinside.txt', 'r') as f:
        deadinside_items = list(map(str.strip, f.readlines()))
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=random.choice(deadinside_items))
# TODO: think of a best way to deal with data files
# TODO: refactor function to be more compact and extensible
