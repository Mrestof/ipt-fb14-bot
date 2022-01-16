import requests
import os

from bs4 import BeautifulSoup


# TODO: remove duplicates from ero.py
def crawl():
    url = f'https://wallhaven.cc/search?categories=100&purity=100&sorting=random&order=desc'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser")
    s = soup.find('a', {'class': 'preview'})
    filename = (str(s)[48:54])
    filename_part = filename[:2]
    url = f'https://w.wallhaven.cc/full/{filename_part}/wallhaven-{filename}.jpg'
    return url


def url_check(url):
    r = requests.get(url)
    if r.status_code == 404:
        url = url[:-3] + "png"
        return url
    else:
        return url


def download_photo():
    image_info = url_check(crawl())
    filename = image_info[31:47]
    r = requests.get(image_info, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename


def remove_photo(path):
    os.remove(path)
