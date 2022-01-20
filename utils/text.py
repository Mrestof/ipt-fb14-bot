import csv


# Function to remove 'ь' from "Илья"
def ilya_modifier(wordlist, tg_message):
    while any(w in tg_message.lower() for w in wordlist):
        for word in wordlist:
            pos = tg_message.lower().find(word)
            # TODO: sort out how this work
            if pos != -1:
                realword = tg_message[pos:pos + len(word)]
                tg_message = tg_message.replace(realword, realword.replace('ь', '').replace('Ь', ''))
    return tg_message


# Function to remove "ний" from "Разумний"
def razum_modifier(wordlist, tg_message):
    while any(w in tg_message.lower() for w in wordlist):
        for word in wordlist:
            pos = tg_message.lower().find(word)
            # TODO: sort out how this work
            if pos != -1:
                realword = tg_message[pos:pos + len(word)]
                pos2 = realword.lower().find("н")
                tg_message = tg_message.replace(realword, realword[:pos2])
    return tg_message


# Function to write 5 important messages to file
def important_data_write(text: str) -> None:
    saved_msgs_path = 'data/saved_msgs.csv'
    with open(saved_msgs_path, 'r') as f:
        rows = list(csv.DictReader(f))

    if len(rows) == 5:
        _ = rows.pop(0)

    new_row = {'msg_text': text}
    rows.append(new_row)
