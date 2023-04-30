# TODO: explain magic numbers or refactor the blocks of code with them or refactor the whole module
import random
import requests
import os

from PIL import Image
from bs4 import BeautifulSoup
from NHentai import NHentai


# TODO: rewrite
def crawl(images_type):
    url = ''
    if images_type == 'photo':
        url = 'https://wallhaven.cc/search?categories=100&purity=100&ratios=16x9&topRange=1y&sorting=toplist&order' \
              f'=desc&page={random.randint(1, 100)} '
    elif images_type == 'ero':
        url = 'https://wallhaven.cc/search?categories=001&purity=010&topRange=1y&sorting=toplist&order=desc&page=' \
              f'{random.randint(1, 300)}'
    elif images_type == 'ecchi':
        url = 'https://wallhaven.cc/search?categories=010&purity=010&topRange=1y&sorting=toplist&order=desc&page=' \
              f'{random.randint(1, 300)}'
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


# TODO: somehow save the useful info on fail of this function
def url_check(url):
    r = requests.get(url)
    if r.status_code == 404:
        url = url[:-3] + "png"
    return url


def download_wallhaven(image_type):
    image_url = url_check(crawl(image_type))
    filename = image_url[31:47]
    os.system(f'wget --limit-rate=2m -O {filename} {image_url}')
    return filename


# TODO: redo using more than 1 brain cell (try implementing with custom `with` API)
def remove_file(path):
    os.remove(path)


def resize_image(path, max_size):
    # TODO: cut indents
    if os.path.isfile(path):
        try:
            im = Image.open(path)
            if im.height > max_size or im.width > max_size:
                f, e = os.path.splitext(path)

                # if width > height:
                if im.width > im.height:
                    desired_width = max_size
                    desired_height = im.height / (im.width / max_size)

                # if height > width:
                elif im.height > im.width:
                    desired_height = max_size
                    desired_width = im.width / (im.height / max_size)

                else:
                    desired_height = max_size
                    desired_width = max_size

                # convert back to integer
                desired_height = int(desired_height)
                desired_width = int(desired_width)

                im_resized = im.resize((desired_width, desired_height))
                # im_resized.save(f + '_resized.jpg', 'JPEG', quality=90) # doesn't overwrite file
                if im.format == 'JPEG':
                    im_resized.save(f + e, 'JPEG', quality=80)  # does overwrite file
                elif im.format == 'PNG':
                    im_resized.save(f + e, 'PNG', quality=80)  # format
                else:
                    print(str(im.format) + ' Unknown format')
                # im_resized.save('resized_' + f + '.jpg', 'JPEG', quality=100)
        except Exception as e:
            print(e)


def download_hentai():
    nhentai = NHentai()
    doujin = nhentai.get_random()
    image_info = doujin.images[0].src  # link to the found picture
    filename = str(doujin.id)
    os.system(f'wget --limit-rate=1m -O {filename} {image_info}')
    return filename
