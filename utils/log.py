import logging

# --------------------------------------------------------------------------
#   Constants
# --------------------------------------------------------------------------
"""
%(name)s            Name of the logger (logging channel)
%(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                    WARNING, ERROR, CRITICAL)
%(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                    "WARNING", "ERROR", "CRITICAL")
%(pathname)s        Full pathname of the source file where the logging
                    call was issued (if available)
%(filename)s        Filename portion of pathname
%(module)s          Module (name portion of filename)
%(lineno)d          Source line number where the logging call was issued
                    (if available)
%(funcName)s        Function name
%(created)f         Time when the LogRecord was created (time.time()
                    return value)
%(asctime)s         Textual time when the LogRecord was created
%(msecs)d           Millisecond portion of the creation time
%(relativeCreated)d Time in milliseconds when the LogRecord was created,
                    relative to the time the logging module was loaded
                    (typically at application startup time)
%(thread)d          Thread ID (if available)
%(threadName)s      Thread name (if available)
%(process)d         Process ID (if available)
%(message)s         The result of record.getMessage(), computed just as
                    the record is emitted
"""

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
