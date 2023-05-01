import json
import datetime

DIARY_DT = dict[str, list[str]]


# TODO: check for file existence
# TODO: split repeating code into functions

def diary_read_one(date: str) -> str:
    response = f'Записи на {date}\n\n'
    date = date.replace('.', '/')

    with open('data/diary.json', 'r') as f:
        diary: DIARY_DT = json.load(f)

    try:
        for pos, notes in enumerate(diary[date]):
            response += f'{pos}: {notes}\n'
        return response
    except KeyError:
        return f'{response}Записів немає'


def diary_read_full() -> str:
    response = ''
    with open('data/diary.json', 'r') as f:
        diary: DIARY_DT = json.load(f)

    dates = sorted(diary.keys(), key=lambda d: datetime.datetime.strptime(d, "%d/%m"))

    for date in dates:
        response += f'Записи на {date}\n'
        for pos, notes in enumerate(diary[date]):
            response += f'{pos}: {notes}\n'
        response += '\n\n'
    return response


def diary_write_one(date: str, notes: str) -> str:
    date = date.replace('.', '/')
    try:
        day, month = date.split('/')
        day, month = int(day), int(month)
        date = f'{day}/{month}'
        datetime.datetime(year=datetime.datetime.now().year, month=month, day=day)
    except ValueError:
        return 'Вірний формат дати: 31/12 або 31.12'

    with open('data/diary.json', 'r') as f:
        diary: DIARY_DT = json.load(f)

    # TODO: redo with default dict
    if date in diary.keys():
        diary[date].append(notes)
    else:
        diary[date] = [notes]

    with open('data/diary.json', 'w') as f:
        json.dump(diary, f)

    return 'Додано'


def diary_delete_one(date: str, notes_pos: int) -> str:
    date = date.replace('.', '/')

    try:
        notes_pos = int(notes_pos)
        if notes_pos < 0:
            return 'Число не може бути відємне'
        day, month = date.split('/')
        datetime.datetime(year=datetime.datetime.now().year, month=int(month), day=int(day))
    except ValueError:
        return 'Вірний формат дати: 31/12 або 31.12'

    with open('data/diary.json', 'r') as f:
        diary: DIARY_DT = json.load(f)

    if date in diary.keys():
        # TODO: move 0 len check to the end
        if len(diary[date]) == 0:
            diary.pop(date)
        elif len(diary[date]) > notes_pos:
            del diary[date][notes_pos]
        else:
            return 'Такого запису на цю дату немає'
    else:
        return 'Записів на цю дату немає'
    with open('data/diary.json', 'w') as f:
        json.dump(diary, f)

    return 'Видалено'
