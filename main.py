import random

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler

from utils import ilya_ilya, ilya_razum
from hentai import download_hentai, remove_hentai

with open('token.txt', 'r') as f:
    token = f.readline().strip()
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def text_messages(update: Update, context: CallbackContext) -> None:

    tg_message = update.message.text
    tg_message_id = update.message.message_id
    tg_user = update.message.from_user

    wordlist_ilya = ['илья', 'ильи', 'илье', 'илью', 'ильей', 'ильёй']
    wordlist_razum = ['разумный', 'разумного', 'разумным', 'разумному', 'разумная']
    wordlist_kringe = ['кринж', 'криндж']
    send = False
    if 'выполнить приказ 66' in tg_message.lower():
        # context.bot.kickChatMember(chat_id=update.effective_chat.id, user_id='483029014')
        context.bot.leaveChat(chat_id=update.effective_chat.id)
        return None
    if '@hhanchenn' in tg_message.lower():
        context.bot.send_message(chat_id=update.effective_chat.id, text='хахачлен', reply_to_message_id=tg_message_id)
        return None
    if tg_message.lower() == 'оск' or ' оск ' in tg_message.lower():
        osk_list = ['орбление', 'Оски (Osci, Opsci, Όσκοι, Όπικοί) — считавшие себя италийскими автохтонами, '
                                'составляли ветвь умбрийского племени и занимали, в доисторическую эпоху, '
                                'Среднюю Италию, часть Лация и Кампанию.', 'Может сразу голосовые кидать, если писать '
                                                                           'сложно?']
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(osk_list),
                                 reply_to_message_id=tg_message_id)
        return None
    if any(c in tg_message.lower() for c in wordlist_kringe):
        kringe_list = ['КРИИИИИИИИНЖ', 'Кринжовый кринж, кринжанул', f'{tg_user.first_name} опять кринжанул и '
                                                                     f'сморозил херню', 'ИСПАНСКИЙ СТЫД']
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(kringe_list), reply_to_message_id=tg_message_id)
        return None
    if any(c in tg_message.lower() for c in wordlist_ilya):
        tg_message = ilya_ilya(wordlist_ilya, tg_message)
        send = True
    if any(c in tg_message.lower() for c in wordlist_razum):
        tg_message = ilya_razum(wordlist_razum, tg_message)
        send = True
    if send:
        reply_list = ['Блядь, опять херню пишешь', 'Ты в школе вообще учился?',
                      'Это знать надо! Если ты учился на ФизТехе. Это классика, блядь!']
        reply = random.choice(reply_list) + '\n' + 'Правильно будет: ' + tg_message
        # работает без str, но предупреждение из-за какой-то хуйни в либе
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply, reply_to_message_id=tg_message_id)


def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ну да, хуевый у меня ник.\nНо это блядь не значит '
                                                                    'что на него тыкать нужно!')


def hentai(update: Update, context: CallbackContext) -> None:
    path = download_hentai()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'))
    remove_hentai(path)


pasha_nick_handler = CommandHandler('I3700ch1u', pasha_nick)
dispatcher.add_handler(pasha_nick_handler)

hentai_handler = CommandHandler('hentai', hentai)
dispatcher.add_handler(hentai_handler)

text_handler = MessageHandler(Filters.text & (~Filters.command), text_messages)
dispatcher.add_handler(text_handler)

updater.start_polling()
