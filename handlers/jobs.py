import datetime
import requests
from data.birthdays import fb14_birthday_dates_to_names
from telegram.ext import CallbackContext
from utils.diary import diary_delete_date


async def birthday_check(context: CallbackContext) -> None:
    fb14_chatid = -1001698562626  # toconf
    today = datetime.date.today()
    week_ahead = today + datetime.timedelta(days=+7)
    week_ahead_date = week_ahead.strftime('%d/%m')
    try:
        await context.bot.send_message(
            chat_id=fb14_chatid,
            text='Через тиждень день народження у '+' та '.join(fb14_birthday_dates_to_names[week_ahead_date])
        )
    except KeyError:
        return None


async def update_schedule(context: CallbackContext) -> None:
    url = 'http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=aaa20291-ed32-46ad-b75f-853fb7480aa6'
    response = requests.get(url)
    try:
        with open('data/schedule/schedule.html', 'w') as file:
            file.write(response.text)
    except FileNotFoundError as e:
        print(f'Could not write to a file; Error: {e}')


async def diary_remove_day(_: CallbackContext) -> None:
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)
    yesterday_date = yesterday.strftime('%d/%m')
    diary_delete_date(yesterday_date)
