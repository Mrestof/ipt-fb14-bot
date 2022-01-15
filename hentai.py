import random
import requests
import os


def Generate_Code():  # function generates a random 6 digit number
    code = ''
    for i in range(6):
        code += str(random.randint(0, 9))
    return code


def valid_url():  # function checks whether a doujin exists with the generated code
    url = None
    valid = False
    while not valid:
        url = 'https://nhentai.net/g/' + Generate_Code() + '/1/'
        r = requests.get(url)
        if r.status_code != 404:
            valid = True
    return url


def getlink():
    r = (requests.get(valid_url()))
    pos1 = r.content.decode().find('https://i.nhentai.net/galleries')
    pos2 = r.content.decode()[pos1:].find('"')
    return r.content.decode()[pos1:pos1 + pos2]


def download_hentai():
    image_url = getlink()
    filename = image_url.split("/")[-2]
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename


def remove_hentai(path):
    os.remove(path)
