#!/bin/env python3.11

from utils.log import get_main_logger
from utils.init import get_token, get_application, set_commands


def main():
    logger = get_main_logger()

    token = get_token()  # Getting Bot Token from a file

    application = get_application(token)  # Bot application (Function for initiation)

    # set_commands(application, token)  # Setting commands description

    logger.info('Start the bot. Logs go here.')
    application.run_polling()  # Bot Start Function


def debug():
    ...


if __name__ == '__main__':
    main()
