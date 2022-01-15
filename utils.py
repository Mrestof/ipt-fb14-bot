def ilya_ilya(wordlist1, tg_message):
    while any(c in tg_message.lower() for c in wordlist1):
        for word in wordlist1:
            pos = tg_message.lower().find(word)
            if pos != -1:  # оно и без этого работает не багаясь почему-то, но пусть будет
                realword = tg_message[pos:pos + len(word)]
                tg_message = tg_message.replace(realword, realword.replace('ь', '').replace('Ь', ''))
    return tg_message


def ilya_razum(wordlist2, tg_message):
    while any(c in tg_message.lower() for c in wordlist2):
        for word in wordlist2:
            pos = tg_message.lower().find(word)
            if pos != -1:  # оно и без этого работает не багаясь почему-то, но пусть будет
                realword = tg_message[pos:pos + len(word)]
                pos2 = realword.lower().find("н")
                tg_message = tg_message.replace(realword, realword[:pos2])
    return tg_message


'''
def izvrashenie(tg_message: str):
    wordlist = ['илья', 'ильи', 'илье', 'илью', 'ильей']
    while any(c in tg_message.lower() for c in wordlist):
        for word in wordlist:
            tg_message = tg_message.replace(tg_message[tg_message.lower().find(word):tg_message.lower().find(word) + len(word)], tg_message[tg_message.lower().find(word):tg_message.lower().find(word) + len(word)].replace('ь', '').replace('Ь', ''))
    return tg_message

print(izvrashenie("Илья Илья Илья ИЛкакдалаья . что делает Илья в да ИЛье ИЛЬЮ"))
'''