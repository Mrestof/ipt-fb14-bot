import random

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler

from utils import ilya_ilya, ilya_razum
from hentai import download_hentai, remove_hentai

# with open('token.txt', 'r') as f:
#    token = f.readline()
with open('token.txt', 'r') as f:
    token = f.readline().strip()
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def ilya(update: Update, context: CallbackContext) -> None:
    tg_message = update.message.text
    tg_user = update.message.from_user
    wordlist1 = ['илья', 'ильи', 'илье', 'илью', 'ильей', 'ильёй']
    wordlist2 = ['разумный', 'разумного', 'разумным', 'разумному', 'разумная']
    send = False
    if 'выполнить приказ 66' in tg_message.lower():
        # context.bot.kickChatMember(chat_id=update.effective_chat.id, user_id='483029014')
        context.bot.leaveChat(chat_id=update.effective_chat.id)
        return None
    if 'кринж' in tg_message.lower() or 'криндж' in tg_message.lower():
        kringe_list = ['КРИИИИИИИИНЖ', 'Кринжовый кринж, кринжанул']
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(kringe_list))
        return None
    if any(c in tg_message.lower() for c in wordlist1):
        tg_message = ilya_ilya(wordlist1, tg_message)
        send = True
    if any(c in tg_message.lower() for c in wordlist2):
        tg_message = ilya_razum(wordlist2, tg_message)
        send = True
    if send:
        reply = str(tg_user['first_name']) + ' блять опять херню пишет' + '\n' + 'Правильно будет: ' + tg_message
        # работает без str, но предупреждение из-за какой-то хуйни в либе
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Нахрена ты на мой ник тыкаешь?')


def hentai(update: Update, context: CallbackContext) -> None:
    path = download_hentai()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'))
    remove_hentai(path)


pasha_nick_handler = CommandHandler('I3700ch1u', pasha_nick)
dispatcher.add_handler(pasha_nick_handler)

hentai_handler = CommandHandler('hentai', hentai)
dispatcher.add_handler(hentai_handler)  # выключено

ilya_handler = MessageHandler(Filters.text & (~Filters.command), ilya)
dispatcher.add_handler(ilya_handler)

updater.start_polling()
