from bs4 import BeautifulSoup, ResultSet
from data.schedule.links import subject_to_link
from utils.log import get_logger

logger = get_logger(__name__)


def _get_subjects_and_professors(a_tags: ResultSet) -> tuple[str, tuple[str, str]]:
    logger.debug('start func')

    subject = ''
    professor = ''
    for a_tag in a_tags:
        href = a_tag.get('href')
        if href.startswith('http'):
            subject += f'{a_tag.text} '
        else:
            professor += f'{a_tag.text} '

    if subject and professor:
        try:
            link_tuple = subject_to_link[subject.strip()]
            return f'{subject}\n{professor}\n', link_tuple
        except KeyError:
            return f'{subject}\n{professor}', ('', '')

    return '', ('', '')


def _is_first_week_current(tr_tags: ResultSet) -> bool:
    logger.debug('start func')

    for tr in tr_tags:
        if tr.find('td', class_='day_backlight') is not None:
            return True
    return False


def _find_a_class(td_tags: ResultSet) -> int:
    logger.debug('start func')

    # If a tag has class attribute - its index is the day option
    for index, td in enumerate(td_tags):
        if td.get('class') is not None:
            return index

    return -1


def _find_current_day(table_tags: ResultSet) -> int:
    logger.debug('start func')

    for table_tag in table_tags:
        tr_tags = table_tag.find_all('tr')
        for tr in tr_tags:
            td_tags = tr.find_all('td')
            index = _find_a_class(td_tags)
            if index != -1:
                return index
    return -1


def _output_day(
        html: str,
        is_this_week: bool,
        is_next_day: bool,
        option: int = -1
) -> str:
    logger.debug('start func, is_this_week=%s, is_next_day=%s, option=%d', is_this_week, is_next_day, option)

    schedule = ''
    # Create a new instance of the BeautifulSoup class from the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Find all needed tags in the HTML content
    table_tags = soup.find_all('table')
    if option == -1:
        option = _find_current_day(table_tags)
    if is_next_day and option < 6:
        option += 1
    elif is_next_day:
        option = 1
        is_this_week = False

    tr_tags = table_tags[0].find_all('tr')
    is_first_week_current = _is_first_week_current(tr_tags)
    if (not is_this_week and is_first_week_current) or (is_this_week and not is_first_week_current):
        tr_tags = table_tags[1].find_all('tr')

    # Inside tr tags extract useful information from td tags
    for index, tr in enumerate(tr_tags):
        td_tags = tr.find_all('td')

        subject_type = ''
        if index == 0:
            day = f'{td_tags[option].text}\n\n'
            schedule += day
        else:
            td_text = td_tags[option].text.split()
            if td_text:
                subject_type = ' '.join(td_text[-2:])

        a_tags = td_tags[option].find_all('a')
        subjects_and_professors, link_type = _get_subjects_and_professors(a_tags)

        link = ''
        if subject_type.strip() == 'Лек on-line':
            link = link_type[0]
        else:
            link = link_type[1]
        if subjects_and_professors != '':
            time = td_tags[0].text[1:]
            schedule += f'{time}. {subject_type}\n{subjects_and_professors}лінк: {link}\n\n'

    return schedule


def get_schedule(
        *,
        day: str = '',
        is_this_week=True,
        is_next_day=False
) -> str:
    logger.debug('start func, day=%s, is_this_week=%s, is_next_day=%s', day, is_this_week, is_next_day)

    try:
        with open('data/schedule/schedule.html', 'r') as file:
            template = file.read()
    except FileNotFoundError as e:
        logger.error(e)
        return 'There is a server problem. contact an admin'

    options: dict[str, int] = {
        'пн': 1, 'вт': 2, 'ср': 3, 'чт': 4, 'пт': 5, 'сб': 6
    }

    if day == '':
        return _output_day(template, is_this_week, is_next_day)
    if day not in options:
        return 'Введіть день у форматі "пн", "вт", "ср", "чт", "пт", "сб"'
    option = options[day]

    return _output_day(template, is_this_week, is_next_day, option=option)
