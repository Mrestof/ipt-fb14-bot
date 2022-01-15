import csv


def ilya_ilya(wordlist, tg_message):
    while any(w in tg_message.lower() for w in wordlist):
        for word in wordlist:
            pos = tg_message.lower().find(word)
            # TODO: sort out why the following line is not required
            if pos != -1:
                realword = tg_message[pos:pos + len(word)]
                tg_message = tg_message.replace(realword, realword.replace('ь', '').replace('Ь', ''))
    return tg_message


def ilya_razum(wordlist, tg_message):
    while any(w in tg_message.lower() for w in wordlist):
        for word in wordlist:
            pos = tg_message.lower().find(word)
            # TODO: sort out why the following line is not required
            if pos != -1:
                realword = tg_message[pos:pos + len(word)]
                pos2 = realword.lower().find("н")
                tg_message = tg_message.replace(realword, realword[:pos2])
    return tg_message


def important_data_write(text: str) -> None:
    saved_msgs_path = 'data/saved_msgs.csv'
    with open(saved_msgs_path, 'r') as f:
        rows = list(csv.DictReader(f))

    if len(rows) == 5:
        _ = rows.pop(0)

    new_row = {'msg_text': text}
    rows.append(new_row)
