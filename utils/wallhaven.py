import random
import requests
import os
import tempfile

from bs4 import BeautifulSoup


def crawl(images_type):
    url = ''  # нужно ли это?
    if images_type == 'photo':
        url = f'https://wallhaven.cc/search?categories=100&purity=100&ratios=16x9&topRange=1y&sorting=toplist&order' \
              f'=desc&page={random.randint(1, 50)} '
    elif images_type == 'ero':
        url = f'https://wallhaven.cc/search?categories=001&purity=010&topRange=1y&sorting=toplist&order=desc&page=' \
              f'{random.randint(1, 100)}'
    elif images_type == 'ecchi':
        url = f'https://wallhaven.cc/search?categories=010&purity=010&topRange=1y&sorting=toplist&order=desc&page=' \
              f'{random.randint(1, 100)}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    ss = soup.findAll('a', {'class': 'preview'})
    filename_list = []
    for s in ss:
        filename = (str(s)[48:54])
        filename_list.append(filename)
    chosen_filename = random.choice(filename_list)
    chosen_filename_part = chosen_filename[:2]
    url = f'https://w.wallhaven.cc/full/{chosen_filename_part}/wallhaven-{chosen_filename}.jpg'
    return url


def url_check(url):
    r = requests.get(url)
    if r.status_code == 404:
        url = url[:-3] + "png"
        return url
    else:
        return url


def download_wallhaven(image_type):
    image_info = url_check(crawl(image_type))
    filename = image_info[31:47]
    r = requests.get(image_info, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename


def remove_wallhaven(path):
    os.remove(path)
