import datetime
from data.birthdays import fb14_birthday_dates_to_names


async def birthday_check(context):
    fb14_chatid = -1001698562626  # toconf
    today = datetime.date.today()
    delta7 = datetime.timedelta(days=+7)
    today7_date = str((today+delta7).day) + '/' + str((today+delta7).month)
    try:
        await context.bot.send_message(
            chat_id=fb14_chatid,
            text='Через тиждень день народження у '+' та '.join(fb14_birthday_dates_to_names[today7_date])
        )
    except KeyError:
        return None
