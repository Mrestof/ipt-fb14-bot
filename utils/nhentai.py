import random
import requests
import os


# function generates a random 6-digit number
def Generate_Code():
    code = ''
    for i in range(6):
        code += str(random.randint(0, 9))
    return code


# function checks whether a doujin exists with the generated code
def valid_url():
    url = None
    valid = False
    while not valid:
        url = 'https://nhentai.net/g/' + Generate_Code() + '/1/'
        r = requests.get(url)
        if r.status_code != 404:
            valid = True
    return url


def getlink():
    url = valid_url()
    r = (requests.get(url))
    filename = url.split('/')[-3]
    pos1 = r.content.decode().find('https://i.nhentai.net/galleries')
    pos2 = r.content.decode()[pos1:].find('"')
    return r.content.decode()[pos1:pos1 + pos2], filename


def download_hentai():
    image_info = getlink()
    filename = image_info[1]
    r = requests.get(image_info[0], stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename


def remove_hentai(path):
    os.remove(path)
