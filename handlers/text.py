# TODO: add switches for text functions
# TODO: fix var naming (for commented blocks of code)
import random
import re

from telegram import Update
from telegram.ext import CallbackContext

from utils.text import ilya_modifier, razum_modifier
from tempcfg import order66_state, hhanchenn_state, osk_state, kringe_state, zemlyanoi_state, ilya_state, razum_state, \
    pasha400_state, deadinside_state, khashcha_state


# TODO: research the ways of splitting the big handler into smaller pieces
# TODO: try to merge some conditions into more compact blocks of code
# TODO: put constants to the separate file/var


def text_messages(update: Update, context: CallbackContext) -> None:
    if update.message is None:
        # TODO: fix handling of edited_messages
        return None
    elif update.message.chat.type == 'private':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Chat functions only for groups')
        return None

    tg_message = update.message.text
    tg_message_id = update.message.message_id
    tg_user = update.message.from_user

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
                  f'{tg_user.first_name} ошибся, он Зеленский']
    wordlist_khashcha = ['хаща', 'хащи', 'хаще', 'хащу']
    khashcha_list = ['Ліс', 'Бір', 'Діброва', 'Тундра', 'Тайга', 'Пуща']

    if pasha400_state and len(tg_message) > 400 and tg_user.id == 483029014:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Он опять какую-то херню на пол экрана написал',
                                 reply_to_message_id=tg_message_id)
    if order66_state and 'выполнить приказ 66' in tg_message.lower() and tg_user.id == 483029014:
        context.bot.leaveChat(chat_id=update.effective_chat.id)
        return None

    if hhanchenn_state and '@hhanchenn' in tg_message.lower():
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='хахачлен',
                                 reply_to_message_id=tg_message_id)
        return None

    if osk_state and re.search('[?:,. ]оск[?:,. ]', ' ' + tg_message.lower() + ' ') is not None:
        # TODO: little refactor for regex
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(osk_list),
                                 reply_to_message_id=tg_message_id)
        return None

    if kringe_state and any(c in tg_message.lower() for c in wordlist_kringe):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(kringe_list),
                                 reply_to_message_id=tg_message_id)
        return None

    if zemlyanoi_state and any(c in tg_message.lower() for c in wordlist_earth):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(earth_list),
                                 reply_to_message_id=tg_message_id)
        return None

    if deadinside_state and '1000-7' in tg_message:
        if random.randint(0, 1):
            context.bot.send_audio(chat_id=update.effective_chat.id,
                                   audio=open('data/Fem.Love-1000-7.mp3', 'rb'),
                                   reply_to_message_id=tg_message_id)
        else:
            context.bot.send_audio(chat_id=update.effective_chat.id,
                                   audio=open('data/Fem.Love-Zakat.mp3', 'rb'),
                                   reply_to_message_id=tg_message_id)
    if khashcha_state and any(c in tg_message.lower() for c in wordlist_khashcha):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(khashcha_list),
                                 reply_to_message_id=tg_message_id)
        return None
    send = False
    if ilya_state and any(c in tg_message.lower() for c in wordlist_ilya):
        tg_message = ilya_modifier(wordlist_ilya, tg_message)
        send = True
    if razum_state and any(c in tg_message.lower() for c in wordlist_razum):
        tg_message = razum_modifier(wordlist_razum, tg_message)
        send = True
    if send:
        reply = random.choice(reply_list) + '\n' + 'Правильно будет: ' + tg_message
        # работает без str, но предупреждение из-за какой-то хуйни в либе
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=reply,
                                 reply_to_message_id=tg_message_id)
