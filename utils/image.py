import random
import requests
import os

from PIL import Image
from bs4 import BeautifulSoup
from NHentai import NHentai


def crawl(images_type) -> str:
    url = ''
    photo_page_range = (1, 100)
    ero_page_range = (1, 300)
    ecchi_page_range = (1, 300)
    wallhaven_link = (
        'https://wallhaven.cc/search'
        '?categories={ctg}&purity={pur}&topRange=1y&sorting=toplist&order=desc&page={page}'
    )

    match images_type:
        case 'photo':
            url = wallhaven_link.format(ctg='100', pur='100', page=random.randint(*photo_page_range))
        case 'ero':
            url = wallhaven_link.format(ctg='001', pur='010', page=random.randint(*ero_page_range))
        case 'ecchi':
            url = wallhaven_link.format(ctg='010', pur='010', page=random.randint(*ecchi_page_range))

    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    a_tags = soup.findAll('a', {'class': 'preview'})

    file_id_list = []
    file_id_tag_slice = slice(48, 54)
    for a_tag in a_tags:
        file_id = (str(a_tag)[file_id_tag_slice])
        file_id_list.append(file_id)
    chosen_file_id = random.choice(file_id_list)
    chosen_file_id_part = chosen_file_id[:2]  # wallhaven creates subdirectories by first 2 letters of image's id
    url = f'https://w.wallhaven.cc/full/{chosen_file_id_part}/wallhaven-{chosen_file_id}.jpg'
    return url


def url_check(url) -> str:
    r = requests.get(url)
    if r.status_code != 200:
        url = url[:-3] + "png"
    return url


def download_wallhaven(image_type) -> str:
    image_url = url_check(crawl(image_type))
    filename_slice = slice(31, 47)
    filename = image_url[filename_slice]
    os.system(f'wget --limit-rate=2m -O {filename} {image_url}')
    return filename


def remove_file(path):
    os.remove(path)


def resize_image(path, max_size):
    try:
        im = Image.open(path)
        if not im.height > max_size or not im.width > max_size:
            return None

        f, e = os.path.splitext(path)

        if im.width > im.height:
            desired_width = max_size
            desired_height = im.height / (im.width / max_size)

        elif im.height > im.width:
            desired_height = max_size
            desired_width = im.width / (im.height / max_size)

        else:
            desired_height = max_size
            desired_width = max_size

        desired_height = int(desired_height)
        desired_width = int(desired_width)

        im_resized = im.resize((desired_width, desired_height))
        if im.format == 'JPEG':
            im_resized.save(f + e, 'JPEG', quality=80)  # does overwrite file
        elif im.format == 'PNG':
            im_resized.save(f + e, 'PNG', quality=80)  # format
        else:
            print(str(im.format) + ' Unknown format')
    except Exception as e:
        print(e)


def download_hentai():
    nhentai = NHentai()
    doujin = nhentai.get_random()
    image_info = doujin.images[0].src  # link to the found picture
    filename = str(doujin.id)
    os.system(f'wget --limit-rate=1m -O {filename} {image_info}')
    return filename
