import logging

# --------------------------------------------------------------------------
#   Constants
# --------------------------------------------------------------------------
TOPLEVEL_LOGGER_NAME = 'main'
JSON_LOG_FORMAT_ATTRS = (
    'asctime', 'levelname',
    'filename', 'funcName', 'lineno',
    'message',
)


# TODO: refactor this cringe piece
def _wrap(attr_name: str) -> str:
    json_attrs_to_wrap = ("name", "levelno", "levelname", "pathname", "filename",
                          "module", "funcName", "asctime", "threadName", "message")
    br = '"' if attr_name in json_attrs_to_wrap else ''
    return br+'{' + attr_name + '}'+br


JSON_LOG_FORMAT = '{{' + ','.join(f'"{attr}":{_wrap(attr)}' for attr in JSON_LOG_FORMAT_ATTRS) + '}}'


# ---------------------------------------------------------------------------
#   Utilities
# ---------------------------------------------------------------------------
def get_logger_name(module_name: str) -> str:
    """Append the correct parent logger to the logger name

    :param module_name: name from `__name__` variable
    :return:
    """
    return f'{TOPLEVEL_LOGGER_NAME}.{module_name}'


def get_main_logger(
        name: str = TOPLEVEL_LOGGER_NAME,
        level: int = logging.DEBUG,
        log_format: str = JSON_LOG_FORMAT,
) -> logging.Logger:
    formatter = logging.Formatter(fmt=log_format, style='{')

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(stream_handler)

    logger.info('Initialized the main logger')
    return logger
