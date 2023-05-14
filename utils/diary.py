import json
import datetime

DIARY_DT = dict[str, list[str]]


def diary_read_one_date(date: str) -> str:
    check_result, check_date = diary_check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    diary = diary_read_file()

    response = f'Записи на {date}\n\n'

    try:
        notes_list = diary[date]
    except KeyError:
        response += 'Записів немає'
    else:
        for pos, notes in enumerate(notes_list):
            response += f'{pos}: {notes}\n'
    return response


def diary_read_full() -> str:
    response = ''
    diary = diary_read_file()

    dates = sorted(diary.keys(), key=lambda d: datetime.datetime.strptime(d, "%d/%m"))

    for date in dates:
        response += f'Записи на {date}\n'
        for pos, notes in enumerate(diary[date]):
            response += f'{pos}: {notes}\n'
        response += '\n\n'
    return response if response else 'Помилка'


def diary_write_one_note(date: str, notes: str) -> str:

    check_result, check_date = diary_check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    if len(notes) > 100:
        return 'Довжина запису більше 100 символів'

    diary = diary_read_file()

    if date in diary.keys():
        diary[date].append(notes)
    else:
        diary[date] = [notes]

    diary_write_file(diary)

    return 'Додано'


def diary_delete_one_note(date: str, notes_pos: str) -> str:
    date = date.replace('.', '/')

    if not notes_pos.isdigit():
        return "Номер запису невірний"
    notes_pos = int(notes_pos)

    check_result, check_date = diary_check_date(date)
    if not check_result:
        return check_date
    else:
        date = check_date

    diary = diary_read_file()

    if date in diary.keys():
        if len(diary[date]) > notes_pos:
            del diary[date][notes_pos]
            if len(diary[date]) == 0:
                diary.pop(date)
        else:
            return 'Цього запису на цю дату немає'
    else:
        return 'Записів на цю дату немає'

    diary_write_file(diary)

    return 'Видалено'


def diary_delete_date(date: str) -> str:
    date = date.replace('.', '/')

    check_result, check_date = diary_check_date(date)

    if not check_result:
        return check_date
    else:
        date = check_date

    diary = diary_read_file()

    if date in diary.keys():
        diary.pop(date)
    else:
        return 'Записів на цю дату немає'

    diary_write_file(diary)

    return 'Видалено'


def diary_read_file() -> DIARY_DT:
    try:
        with open('data/diary.json', 'r') as f:
            diary: DIARY_DT = json.load(f)
        return diary
    except FileNotFoundError:
        return DIARY_DT()


def diary_write_file(diary: DIARY_DT):
    with open('data/diary.json', 'w') as f:
        json.dump(diary, f)


def diary_check_date(date: str) -> (bool, str):
    try:
        date = date.replace('.', '/')
        day, month = date.split('/')
        day, month = int(day), int(month)
        date = f'{day}/{month}'
        datetime.datetime(year=datetime.datetime.now().year, month=month, day=day)
        return True, date
    except ValueError:
        return False, 'Вірний формат дати: 7/12 або 7.12'
