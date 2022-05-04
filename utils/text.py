# Function to remove 'ь' from "Илья"
def ilya_modifier(wordlist, tg_message):
    while any(w in tg_message.lower() for w in wordlist):
        for word in wordlist:
            pos = tg_message.lower().find(word)
            if pos != -1:  # check if `word` found
                realword = tg_message[pos:pos + len(word)]
                tg_message = tg_message.replace(realword, realword.replace('ь', '').replace('Ь', ''), -1)
    return tg_message


# Function to remove "ний" from "Разумний"
def razum_modifier(wordlist, tg_message):
    while any(w in tg_message.lower() for w in wordlist):
        for word in wordlist:
            pos = tg_message.lower().find(word)
            if pos != -1:
                realword = tg_message[pos:pos + len(word)]
                pos2 = realword.lower().find("н")
                tg_message = tg_message.replace(realword, realword[:pos2])
    return tg_message
