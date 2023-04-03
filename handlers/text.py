import random
import re

from telegram import Update
from telegram.ext import ContextTypes

from utils.text import ilya_modifier, razum_modifier
from config import *


# TODO: research the ways of splitting the big handler into smaller pieces
# TODO: try to merge some conditions into more compact blocks of code
# TODO: put constants to the separate file/var

async def text_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.edited_message is not None:
        return None

    message_text = update.message.text
    message_id = update.message.message_id
    user = update.message.from_user

    wordlist_ilya = ['илья', 'ильи', 'илье', 'илью', 'ильей', 'ильёй']
    wordlist_razum = ['разумный', 'разумного', 'разумным', 'разумному', 'разумная']
    reply_list = [f'{user.first_name} бредит', 'Блядь, опять херню пишешь', 'Ты в школе вообще учился?',
                  'Это знать надо! Если ты учился на ФизТехе. Это классика, блядь!']
    wordlist_kringe = ['кринж', 'криндж', 'кринге', 'крінж', 'кріндж', 'крінге']
    osk_list = ['орбление', 'Оски (Osci, Opsci, Όσκοι, Όπικοί) — считавшие себя италийскими автохтонами, '
                            'составляли ветвь умбрийского племени и занимали, в доисторическую эпоху, '
                            'Среднюю Италию, часть Лация и Кампанию.', 'Може одразу голосові відправляти, якщо писать '
                                                                       'складно?', 'образа']
    kringe_list = ['КРІІІІІІІІІІНЖ', 'Крінжовый крінж, крінжанув', f'{user.first_name} знову крінжанув та й '
                                                                   f'ляпнув нісенітницю', 'ІСПАНСЬКИЙ СОРОМ']
    wordlist_khashcha = ['хаща', 'хащи', 'хаще', 'хащу', 'хащі', 'хащою', 'хащо']
    khashcha_list = ['Ліс', 'Бір', 'Діброва', 'Тундра', 'Тайга', 'Пуща', 'Дубина', 'Нетрища', 'Гуща']
    kiva_reply = ['Москаляку на гілляку', 'Бан нахуй', 'Вийди з чату', 'Кива пидор ипанный (c) Макуха']
    poroshenko_reply = ['За каденції Петра Олексійовича', 'За каденції Петра Порошенка']

    if pasha400_state and len(message_text) > 300 and user.id == 483029014:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='Він знову якусь фігню на пів екрану написав',
                                       reply_to_message_id=message_id)
        return None

    if tihenko_state and message_text.isupper() and len(message_text) >= 8:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='Тихенько, дитино',
                                       reply_to_message_id=message_id)
        return None
    if order66_state and 'виконати наказ 66' in message_text.lower() and user.id == 483029014:
        await context.bot.leaveChat(chat_id=update.effective_chat.id)
        return None

    if order69_state and 'виконати наказ 69' in message_text.lower() and user.id:
        await context.bot.ban_chat_member(chat_id=update.effective_chat.id,
                                          user_id=658890395)
        return None

    if hhanchenn_state and '@hhanchenn' in message_text.lower():
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='хахачлен',
                                       reply_to_message_id=message_id)
        return None

    if osk_state and re.search(r'\Wоск\W', ' ' + message_text.lower() + ' ') is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=random.choice(osk_list),
                                       reply_to_message_id=message_id)
        return None

    if kringe_state and any(c in message_text.lower() for c in wordlist_kringe):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=random.choice(kringe_list),
                                       reply_to_message_id=message_id)
        return None

    if khashcha_state and any(c in message_text.lower() for c in wordlist_khashcha):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=random.choice(khashcha_list),
                                       reply_to_message_id=message_id)
        return None

    if poroshenko_state and random.randint(0, 100) == 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=random.choice(poroshenko_reply))
        return None

    send = False
    if ilya_state and any(c in message_text.lower() for c in wordlist_ilya):
        message_text = ilya_modifier(wordlist_ilya, message_text)
        send = True
    if razum_state and any(c in message_text.lower() for c in wordlist_razum):
        message_text = razum_modifier(wordlist_razum, message_text)
        send = True
    if send:
        reply = random.choice(reply_list) + '\n' + 'Правильно буде: ' + message_text
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=reply,
                                       reply_to_message_id=message_id)
        return None
    if update.message.forward_from_chat is not None:
        if kiva_state and update.message.forward_from_chat.id == -1001235238484:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=random.choice(kiva_reply),
                                           reply_to_message_id=message_id)
            return None
