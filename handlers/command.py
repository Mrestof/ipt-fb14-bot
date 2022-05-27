from telegram import Update
from telegram.ext import CallbackContext

from utils.markov_chains import markov_sentence


def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Ну тай, хуйовий в мене нік.\nАле це бляха не значить що на нього тикати потрібно!')


def makuha_markov(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=markov_sentence('data/users_messages/658890395') + ' (c) Макуха')
