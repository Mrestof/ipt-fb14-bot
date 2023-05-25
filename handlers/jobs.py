import datetime
import json
import requests
from utils.log import get_logger
from telegram.ext import CallbackContext
from utils.diary import delete_one_date, read_one_date
from utils.text import escape_tg_markdown
from config import fb14_birthday_dates_to_names

logger = get_logger(__name__)


async def birthday_check(context: CallbackContext) -> None:
    logger.info('executed birthday_check')
    fb14_chatid = -1001698562626  # toconf
    today = datetime.date.today()
    week_ahead = today + datetime.timedelta(days=+7)
    week_ahead_date = week_ahead.strftime('%d/%m')
    try:
        await context.bot.send_message(
            chat_id=fb14_chatid,
            text='Через тиждень день народження у ' + ' та '.join(fb14_birthday_dates_to_names[week_ahead_date])
        )
    except KeyError:
        return None


async def update_schedule(_: CallbackContext) -> None:
    logger.info('executed update_schedule')
    url = 'http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=aaa20291-ed32-46ad-b75f-853fb7480aa6'
    response = requests.get(url)
    try:
        with open('data/schedule/schedule.html', 'w') as file:
            file.write(response.text)
    except FileNotFoundError as e:
        logger.error(f'Could not write to a file; Error: {e}')


async def diary_remove_day(_: CallbackContext) -> None:
    logger.info('executed diary_remove_day')
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)
    yesterday_date = yesterday.strftime('%d/%m')
    delete_one_date(yesterday_date)


async def diary_remind(context: CallbackContext) -> None:
    logger.info('executed diary_remind')
    fb14_chatid = -1001698562626  # toconf
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=+1)
    tomorrow_date = tomorrow.strftime('%d/%m')
    response = "\n".join(read_one_date(tomorrow_date).split("\n")[1:])  # removes first line with date
    escaped_response = escape_tg_markdown(response)

    try:
        with open('data/diary_remind.json', 'r') as f:
            diary_remind_users: list = json.load(f)
        for userid in diary_remind_users:
            escaped_response += fr'[\|](tg://user?id={userid})'
    except FileNotFoundError:
        logger.error('data/diary_remind.json does not exist')

    if 'Записів немає' not in escaped_response:
        await context.bot.send_message(
            chat_id=fb14_chatid,
            text=f'Завтра буде:\n{escaped_response}',
            parse_mode='MarkdownV2'
        )
