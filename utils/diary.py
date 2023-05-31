import json
import datetime
from utils.log import get_logger

logger = get_logger(__name__)

DIARY_DT = dict[str, list[str]]


def read_one_date(date: str) -> str:
    logger.debug('start func, date=%s', date)

    check_result, check_date = _check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    diary = _read_file()

    response = f'Записи на {date}\n\n'

    try:
        notes_list = diary[date]
    except KeyError:
        response += 'Записів немає'
    else:
        for pos, notes in enumerate(notes_list):
            response += f'{pos}: {notes}\n'
    return response


def read_full() -> str:
    logger.debug('start func')

    response = ''
    diary = _read_file()

    dates = sorted(diary.keys(), key=lambda d: datetime.datetime.strptime(d, "%d/%m"))

    for date in dates:
        response += f'Записи на {date}\n'
        for pos, notes in enumerate(diary[date]):
            response += f'{pos}: {notes}\n'
        response += '\n'
    return response if response else 'Помилка'


def write_one_note(date: str, notes: str) -> str:
    logger.debug('start func, date=%s, notes=%s', date, notes)

    check_result, check_date = _check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    if len(notes) > 100:
        return 'Довжина запису більше 100 символів'

    diary = _read_file()

    if date in diary.keys():
        diary[date].append(notes)
    else:
        diary[date] = [notes]

    _write_file(diary)

    return 'Додано'


def delete_one_note(date: str, notes_pos: str) -> str:
    logger.debug('start func, date=%s, notes_pos=%s', date, notes_pos)

    if not notes_pos.isdigit():
        return "Номер запису невірний"
    notes_pos = int(notes_pos)

    check_result, check_date = _check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    diary = _read_file()

    if date in diary.keys():
        if len(diary[date]) > notes_pos:
            del diary[date][notes_pos]
            if len(diary[date]) == 0:
                diary.pop(date)
        else:
            return 'Цього запису на цю дату немає'
    else:
        return 'Записів на цю дату немає'

    _write_file(diary)

    return 'Видалено'


def delete_one_date(date: str) -> str:
    logger.debug('start func, date=%s', date)

    check_result, check_date = _check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    diary = _read_file()

    if date in diary.keys():
        diary.pop(date)
    else:
        return 'Записів на цю дату немає'

    _write_file(diary)

    return 'Видалено'


def modify(date: str, notes_pos: str, notes: str) -> str:
    logger.debug('start func, date=%s, notes_pos=%s, notes=%s', date, notes_pos, notes)

    if not notes_pos.isdigit():
        return "Номер запису невірний"
    notes_pos = int(notes_pos)

    check_result, check_date = _check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    if len(notes) > 100:
        return 'Довжина запису більше 100 символів'

    diary = _read_file()

    if date in diary.keys():
        if len(diary[date]) > notes_pos:
            diary[date][notes_pos] = notes
        else:
            return 'Цього запису на цю дату немає'
    else:
        return 'Записів на цю дату немає'

    _write_file(diary)

    return 'Модифіковано'


def remind(user_id) -> str:
    try:
        with open('data/diary_remind.json', 'r') as f:
            diary_remind_users: list = json.load(f)

        if user_id not in diary_remind_users:
            diary_remind_users.append(user_id)
            response = 'Вас тепер БУДЕ тегати за день до записів'
        else:
            diary_remind_users.remove(user_id)
            response = 'Вас тепер НЕ БУДЕ тегати за день до записів'

        with open('data/diary_remind.json', 'w') as f:
            json.dump(diary_remind_users, f)

        return response
    except FileNotFoundError as e:
        logger.error(e)


def _read_file() -> DIARY_DT:
    logger.debug('open data/diary.json for read')
    try:
        with open('data/diary.json', 'r') as f:
            diary: DIARY_DT = json.load(f)
        return diary
    except FileNotFoundError as e:
        logger.error(e)
        return DIARY_DT()


def _write_file(diary: DIARY_DT):
    logger.debug('open data/diary.json for write')
    with open('data/diary.json', 'w') as f:
        json.dump(diary, f)


def _check_date(date: str) -> tuple[bool, str]:
    logger.debug('start func, date=%s', date)
    try:
        date = date.replace('.', '/')
        day, month = date.split('/')
        day, month = int(day), int(month)
        date = f'{day}/{month}'
        datetime.datetime(year=datetime.datetime.now().year, month=month, day=day)
        return True, date
    except ValueError:
        return False, 'Вірний формат дати: 7/12 або 7.12'
