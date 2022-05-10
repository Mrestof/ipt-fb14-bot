from telegram import Update
from telegram.ext import CallbackContext


def alive_minute(context: CallbackContext):
    context.bot.send_message(chat_id=context.job.context,
                             text='Bot is alive')


def alive_minute_job(update: Update, context: CallbackContext):
    context.job_queue.run_repeating(alive_minute, interval=60, first=10, context=update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Started')


def kill_jobs(update: Update, context: CallbackContext):
    context.job_queue.stop()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Stopped')
