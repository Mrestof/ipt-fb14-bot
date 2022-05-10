from utils.init import get_token, get_updater, set_commands


def main():
    token = get_token()  # Getting Bot Token from a file

    set_commands(token)  # Setting commands description
    updater = get_updater(token)  # Bot Updater (Function for initiation)
    updater.start_polling()  # Bot Start Function
    print('Start the bot. Logs go here.')
    updater.idle()


def debug():
    ...


if __name__ == '__main__':
    main()
