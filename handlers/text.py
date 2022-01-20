import random
import re

from telegram import Update
from telegram.ext import CallbackContext


# from utils.text import ilya_ilya, ilya_razum


def text_messages(update: Update, context: CallbackContext) -> None:
    if update.message is None:
        # TODO: fix handling of edited_messages
        return None
    elif update.message.chat.type == 'private':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Chat functions only for groups')
        return None

    tg_message = update.message.text
    tg_message_id = update.message.message_id
    tg_user = update.message.from_user

    tg_message_osk = ' '+tg_message+' '
    wordlist_ilya = ['илья', 'ильи', 'илье', 'илью', 'ильей', 'ильёй']
    wordlist_razum = ['разумный', 'разумного', 'разумным', 'разумному', 'разумная']
    wordlist_kringe = ['кринж', 'криндж', 'кринге']
    osk_list = ['орбление', 'Оски (Osci, Opsci, Όσκοι, Όπικοί) — считавшие себя италийскими автохтонами, '
                            'составляли ветвь умбрийского племени и занимали, в доисторическую эпоху, '
                            'Среднюю Италию, часть Лация и Кампанию.', 'Может сразу голосовые кидать, если писать '
                                                                       'сложно?']
    kringe_list = ['КРИИИИИИИИНЖ', 'Кринжовый кринж, кринжанул', f'{tg_user.first_name} опять кринжанул и '
                                                                 f'сморозил херню', 'ИСПАНСКИЙ СТЫД']
    reply_list = [f'{tg_user.first_name} бредит', 'Блядь, опять херню пишешь', 'Ты в школе вообще учился?',
                  'Это знать надо! Если ты учился на ФизТехе. Это классика, блядь!']
    send = False
    if 'выполнить приказ 66' in tg_message.lower() and tg_user.id == 483029014:
        context.bot.leaveChat(chat_id=update.effective_chat.id)
        return None
    '''
    if '@hhanchenn' in tg_message.lower():
        context.bot.send_message(chat_id=update.effective_chat.id, text='хахачлен', reply_to_message_id=tg_message_id)
        return None
    '''
    if re.search('[?:,. ]оск[?:,. ]', tg_message_osk.lower()) is not None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(osk_list),
                                 reply_to_message_id=tg_message_id)
        return None
    if any(c in tg_message.lower() for c in wordlist_kringe):
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(kringe_list),
                                 reply_to_message_id=tg_message_id)
        return None
    '''
    if any(c in tg_message.lower() for c in wordlist_ilya):
        tg_message = ilya_ilya(wordlist_ilya, tg_message)
        send = True
    if any(c in tg_message.lower() for c in wordlist_razum):
        tg_message = ilya_razum(wordlist_razum, tg_message)
        send = True
    if send:
        reply = random.choice(reply_list) + '\n' + 'Правильно будет: ' + tg_message
        # работает без str, но предупреждение из-за какой-то хуйни в либе
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply, reply_to_message_id=tg_message_id)
    '''
