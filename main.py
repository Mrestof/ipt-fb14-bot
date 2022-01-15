from utils.init import get_token, get_updater


def main():
    token = get_token()
    updater = get_updater(token)
    updater.start_polling()


def debug():
    from utils.text import important_data_write
    important_data_write('super cool data \n uberrr')


if __name__ == '__main__':
    main()
