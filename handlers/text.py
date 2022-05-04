import random
import re

from telegram import Update
from telegram.ext import CallbackContext

from utils.text import ilya_modifier, razum_modifier
from config import *


with open('data/fullgroups.txt', 'r') as f:
    fullgroups = [int(i.strip()) for i in f.readlines()]
with open('data/limitgroups.txt', 'r') as f:
    limitgroups = [int(i.strip()) for i in f.readlines()]
with open('data/makuha_kick_list.txt', 'r') as f:
    makuha_kick_id = [int(i.strip()) for i in f.readlines()]

# TODO: research the ways of splitting the big handler into smaller pieces
# TODO: try to merge some conditions into more compact blocks of code
# TODO: put constants to the separate file/var


def text_messages(update: Update, context: CallbackContext) -> None:

    if update.edited_message is not None:
        return None
    elif update.message.chat.type == 'private':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Chat functions only for groups')
        return None
    elif update.message.chat.id not in fullgroups and update.message.chat.id not in limitgroups:
        '''
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Not working')
        '''
        return None

    tg_message = update.message.text
    tg_message_id = update.message.message_id
    tg_user = update.message.from_user
    tg_group_id = update.message.chat.id

    wordlist_ilya = ['илья', 'ильи', 'илье', 'илью', 'ильей', 'ильёй']
    wordlist_razum = ['разумный', 'разумного', 'разумным', 'разумному', 'разумная']
    reply_list = [f'{tg_user.first_name} бредит', 'Блядь, опять херню пишешь', 'Ты в школе вообще учился?',
                  'Это знать надо! Если ты учился на ФизТехе. Это классика, блядь!']
    wordlist_kringe = ['кринж', 'криндж', 'кринге']
    osk_list = ['орбление', 'Оски (Osci, Opsci, Όσκοι, Όπικοί) — считавшие себя италийскими автохтонами, '
                            'составляли ветвь умбрийского племени и занимали, в доисторическую эпоху, '
                            'Среднюю Италию, часть Лация и Кампанию.', 'Может сразу голосовые кидать, если писать '
                                                                       'сложно?']
    kringe_list = ['КРИИИИИИИИНЖ', 'Кринжовый кринж, кринжанул', f'{tg_user.first_name} опять кринжанул и '
                                                                 f'сморозил херню', 'ИСПАНСКИЙ СТЫД']
    wordlist_earth = ['земляной', 'земляного', 'земляному', 'земляным', 'земляном']
    earth_list = ['Нет, блин, лунный', 'Нет, блин, водный', 'Хто Я?', 'Вийди отсюда розбійник!',
                  f'Зеленский']
    wordlist_khashcha = ['хаща', 'хащи', 'хаще', 'хащу']
    khashcha_list = ['Ліс', 'Бір', 'Діброва', 'Тундра', 'Тайга', 'Пуща']

    if (pasha400_state or tg_group_id in fullgroups) and len(tg_message) > 300 and tg_user.id == 483029014:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Он опять какую-то херню на пол экрана написал',
                                 reply_to_message_id=tg_message_id)
        return None
    if (order66_state or tg_group_id in fullgroups) and 'выполнить приказ 66' in tg_message.lower() and tg_user.id == 483029014:
        context.bot.leaveChat(chat_id=update.effective_chat.id)
        return None

    if (order69_state or tg_group_id in fullgroups) and 'виконати наказ 69' in tg_message.lower() and tg_user.id in makuha_kick_id:
        context.bot.ban_chat_member(chat_id=update.effective_chat.id,
                                   user_id=658890395)
        return None

    if (hhanchenn_state or tg_group_id in fullgroups) and '@hhanchenn' in tg_message.lower():
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='хахачлен',
                                 reply_to_message_id=tg_message_id)
        return None

    if (osk_state or tg_group_id in fullgroups) and re.search('[?:,. ]оск[?:,. ]', ' ' + tg_message.lower() + ' ') is not None:
        # TODO: little refactor for regex
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(osk_list),
                                 reply_to_message_id=tg_message_id)
        return None

    if (kringe_state or tg_group_id in fullgroups) and any(c in tg_message.lower() for c in wordlist_kringe):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(kringe_list),
                                 reply_to_message_id=tg_message_id)
        return None

    if (zemlyanoi_state or tg_group_id in fullgroups) and any(c in tg_message.lower() for c in wordlist_earth):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(earth_list),
                                 reply_to_message_id=tg_message_id)
        return None

    if (khashcha_state or tg_group_id in fullgroups) and any(c in tg_message.lower() for c in wordlist_khashcha):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(khashcha_list),
                                 reply_to_message_id=tg_message_id)
        return None

    send = False
    if (ilya_state or tg_group_id in fullgroups) and any(c in tg_message.lower() for c in wordlist_ilya):
        tg_message = ilya_modifier(wordlist_ilya, tg_message)
        send = True
    if (razum_state or tg_group_id in fullgroups) and any(c in tg_message.lower() for c in wordlist_razum):
        tg_message = razum_modifier(wordlist_razum, tg_message)
        send = True
    if send:
        reply = random.choice(reply_list) + '\n' + 'Правильно будет: ' + tg_message
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=reply,
                                 reply_to_message_id=tg_message_id)
        return None

    if (tihenko_state or tg_group_id in fullgroups) and tg_message.isupper() and len(tg_message) >= 8:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Тихенько, дитино',
                                 reply_to_message_id=tg_message_id)
        return None
