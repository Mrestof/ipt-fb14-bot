from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler, Filters

with open('token.txt', 'r') as f:
    token = f.readline()
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def ilya(update: Update, context: CallbackContext) -> None:
    tg_message = update.message.text
    tg_user = update.message.from_user
    wordlist = [' илья ', ' ильи ', ' илье ', ' илью ', ' ильей ']  # ё?. Не поломаются ли от пробелов позиции - на практике вроде нет, но нужно понять как код работает
    if any(c in tg_message.lower() for c in wordlist):  # Этот if нужно убрать, при этом чтобы сообщение не отправлялось
        while any(c in tg_message.lower() for c in wordlist):
            for word in wordlist:
                pos = tg_message.lower().find(word)
                if pos != -1:  # оно и без этого работает не багаясь почему-то, но пусть будет
                    realword = tg_message[pos:pos + len(word)]
                    tg_message = tg_message.replace(realword, realword.replace('ь', '').replace('Ь', ''))
        reply = str(tg_user['first_name'])+': '+tg_message  # работает без str, но предупреждение из-за какой-то хуйни в либе
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


ilya_handler = MessageHandler(Filters.text & (~Filters.command), ilya)
dispatcher.add_handler(ilya_handler)

updater.start_polling()
