from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler, Filters

with open('token.txt', 'r') as f:
    token = f.readline()
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def ilya(update: Update, context: CallbackContext):
    wordlist = ['илья', 'ильи', 'илье', 'илью', 'ильей']
    for word in wordlist:
        if word in update.message.text.lower():
            pos = update.message.text.lower().find(word)
            realword = update.message.text[pos:pos+len(word)]
            context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text.replace(realword, realword.replace('ь', '').replace('Ь', '')))
            break


ilya_handler = MessageHandler(Filters.text & (~Filters.command), ilya)
dispatcher.add_handler(ilya_handler)

updater.start_polling()
