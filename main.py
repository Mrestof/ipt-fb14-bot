from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler
from utils import ilya_ilya, ilya_razum
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
    if any(c in tg_message.lower() for c in wordlist1):
        tg_message = ilya_ilya(wordlist1, tg_message)
        send = True
    if any(c in tg_message.lower() for c in wordlist2):
        tg_message = ilya_razum(wordlist2, tg_message)
        send = True
    if send:
        reply = str(tg_user['first_name'])+' блять опять херню пишет.'+'\n'+'Правильно будет: '+tg_message
        # работает без str, но предупреждение из-за какой-то хуйни в либе
        context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


def pasha_nick(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Нахрена ты на мой ник тыкаешь?")


pasha_nick_handler = CommandHandler('I3700ch1u', pasha_nick)
dispatcher.add_handler(pasha_nick_handler)
ilya_handler = MessageHandler(Filters.text & (~Filters.command), ilya)
dispatcher.add_handler(ilya_handler)

updater.start_polling()
