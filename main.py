#!/bin/env python3.11

from utils.log import get_main_logger
from utils.init import get_token, get_application


# TODO: refactor
#   -minor stuff
#   -variable names
#   -functions descriptons for those which lack it
#   -redo oneliners
# TODO: log everything
# TODO: use formatter (black)
# TODO: create unit test
# TODO: replace os calls with python alternatives
# TODO: type annotate the code
# TODO: take all constants from configs
# TODO: handlers
#   -update the type of `context` argument for callbacks to the new one
#   -move check for edited messages to decorator
#   -guard anything comnig from Update to ensure it is not None

def main():
    logger = get_main_logger()
    token = get_token()  # Getting Bot Token from a file
    application = get_application(token)  # Bot application (Function for initiation)
    logger.info('Start the bot. Logs go here.')
    application.run_polling()  # Bot Start Function


if __name__ == '__main__':
    main()
