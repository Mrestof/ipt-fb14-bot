from utils.init import get_token, get_updater, set_commands


def main():
    token = get_token()

    set_commands(token)
    updater = get_updater(token)
    updater.start_polling()


def debug():
    from utils.text import important_data_write
    important_data_write('super cool data \n uberrr')


if __name__ == '__main__':
    main()
