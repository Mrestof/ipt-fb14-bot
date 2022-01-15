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

def important_data_write(text):
    f = open('important_data', 'r')
    l = f.readlines()
    f.close()
    if len(l) == 5:
        f = open('important_data', 'w')
        for i in range(4):
            f.write(l[i+1])
        f.close()
    f = open('important_data', 'a')
    f.write(text + '\n')
    f.close()
    return
'''
def izvrashenie(tg_message: str):
    wordlist = ['илья', 'ильи', 'илье', 'илью', 'ильей']
    while any(c in tg_message.lower() for c in wordlist):
        for word in wordlist:
            tg_message = tg_message.replace(tg_message[tg_message.lower().find(word):tg_message.lower().find(word) + len(word)], tg_message[tg_message.lower().find(word):tg_message.lower().find(word) + len(word)].replace('ь', '').replace('Ь', ''))
    return tg_message

print(izvrashenie("Илья Илья Илья ИЛкакдалаья . что делает Илья в да ИЛье ИЛЬЮ"))
'''