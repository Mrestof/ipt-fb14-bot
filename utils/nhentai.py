import os
from NHentai import NHentai


def download_hentai():
    nhentai = NHentai()
    Doujin = nhentai.get_random()
    image_info = Doujin.images[0].src
    filename = str(Doujin.id)
    os.system(f'wget --limit-rate=1m -O {filename} {image_info}')  # TODO: check the OS beforehand
    return filename


def remove_hentai(path):
    os.remove(path)

