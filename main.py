#!/bin/env python3.11

from utils.log import get_logger
from utils.init import get_token, get_application


def main():
    logger = get_logger()
    token = get_token()  # Getting Bot Token from a file
    application = get_application(token)  # Bot setup
    logger.info('Start the bot. Logs go here.')
    application.run_polling()  # Bot Start Function


if __name__ == '__main__':
    main()
