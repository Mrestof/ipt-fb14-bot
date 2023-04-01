

async def example(context):
    # TODO: rework chat_id source
    await context.bot.send_message(chat_id='someid',
                                   text='@maybe_available, лс')
