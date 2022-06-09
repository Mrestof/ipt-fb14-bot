from handlers.text import groups


def pavelko_notify(context):
    # TODO: rework chat_id source
    context.bot.send_message(chat_id=groups[0],
                             text='@maybe_available, лс')

