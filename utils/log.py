import logging
from typing import Optional

# ------------------------------------------------------------------------------
#   Constants
# ------------------------------------------------------------------------------
JSON_ATTRS_TO_WRAP = (  # check python `logging` documentation for explanation
    "name", "levelno", "levelname", "pathname", "filename",
    "module", "funcName", "asctime", "threadName", "message"
)

# ------------------------------------------------------------------------------
#   Configs
# ------------------------------------------------------------------------------
TOPLEVEL_LOGGER_NAME = 'main'
LOG_LEVEL = logging.DEBUG
JSON_LOG_FORMAT_ATTRS = (
    'asctime', 'levelname',
    'name', 'filename', 'funcName', 'lineno',
    'message',
)

def _wrap(attr_name: str) -> str:
    """
    Wrap the attribute name in parentheses if the value is of the string format

    :param attr_name: name of the attribute
    :return: attribute name wrapped correctly to preserve the correct JSON format
    """
    br = '"' if attr_name in JSON_ATTRS_TO_WRAP else ''
    return br+'{' + attr_name + '}'+br


JSON_LOG_FORMAT = '{{' \
    + ','.join(f'"{attr}":{_wrap(attr)}' for attr in JSON_LOG_FORMAT_ATTRS) \
    + '}}'


# ------------------------------------------------------------------------------
#   Utilities
# ------------------------------------------------------------------------------
def init_main_logger() -> None:
    # Initialize the module level logger
    formatter = logging.Formatter(fmt=JSON_LOG_FORMAT, style='{')

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(TOPLEVEL_LOGGER_NAME)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(stream_handler)

    logger.info('Initialized the main logger')


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Append the correct parent logger to the logger name and return the logger
    (use this instead of logging.getLogger).

    :param name: name from `__name__` variable
    :param level: logging level of the returned logger
    :param log_format: format of the returned logger
    :return: Logger with the name corresponding to the global hierarchy
    """
    if not logging.getLogger(TOPLEVEL_LOGGER_NAME).hasHandlers():  # FIX: cringe
        init_main_logger()
    if name and name != TOPLEVEL_LOGGER_NAME:
        logger_name = f'{TOPLEVEL_LOGGER_NAME}.{name}'
        logger = logging.getLogger(logger_name)
        logger.debug('Initialized the logger with name %s', logger_name)
        return logger
    return logging.getLogger(TOPLEVEL_LOGGER_NAME)
