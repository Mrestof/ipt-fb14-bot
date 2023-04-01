from utils.log import get_main_logger
from utils.init import get_token, get_updater, set_commands


def main():
    logger = get_main_logger()

    token = get_token()  # Getting Bot Token from a file

    #set_commands(token)  # Setting commands description
    application = get_updater(token)  # Bot Updater (Function for initiation)

    logger.info('Start the bot. Logs go here.')
    application.run_polling()  # Bot Start Function


def debug():
    ...


if __name__ == '__main__':
    main()
