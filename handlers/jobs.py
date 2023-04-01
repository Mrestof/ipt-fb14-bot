from handlers.text import groups


async def example(context):
    # TODO: rework chat_id source
    await context.bot.send_message(chat_id=groups[1],
                                   text='@maybe_available, лс')
