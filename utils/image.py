# TODO: explain magic numbers or refactor the blocks of code with them or refactor the whole module
import random
import requests
import os

from PIL import Image
from bs4 import BeautifulSoup
from NHentai import NHentai


def crawl(images_type):
    url = ''  # нужно ли это?
    if images_type == 'photo':
        url = 'https://wallhaven.cc/search?categories=100&purity=100&ratios=16x9&topRange=1y&sorting=toplist&order' \
              f'=desc&page={random.randint(1, 50)} '
    elif images_type == 'ero':
        url = 'https://wallhaven.cc/search?categories=001&purity=010&topRange=1y&sorting=toplist&order=desc&page=' \
              f'{random.randint(1, 100)}'
    elif images_type == 'ecchi':
        url = 'https://wallhaven.cc/search?categories=010&purity=010&topRange=1y&sorting=toplist&order=desc&page=' \
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


# TODO: refactor in more convenient and stable way
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
    os.system(f'wget --limit-rate=2m -O {filename} {image_info}')
    return filename


def remove_wallhaven(path):
    os.remove(path)



def resize_image(path, max_size):

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
                    im_resized.save(f + e, 'PNG', quality=80)
                else:
                    print(im.format+' Unknown format')
                # im_resized.save('resized_' + f + '.jpg', 'JPEG', quality=100)
        except Exception as e:
            print(e)


def download_hentai():
    nhentai = NHentai()
    Doujin = nhentai.get_random()
    image_info = Doujin.images[0].src  # link to the found picture
    filename = str(Doujin.id)
    os.system(f'wget --limit-rate=1m -O {filename} {image_info}')
    return filename


def remove_hentai(path):
    os.remove(path)