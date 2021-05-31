import os
from PIL import Image

import imghdr
import unidecode
import unicodedata


ARCHIVES_DIRECTORY = r'./archives'
directory = r'./archives'
thumbnail = r'./archives/thumbs'


def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)


def create_thumb(img):
    wpercent = (350/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((350, hsize), Image.ANTIALIAS)
    img = create_square(img)
    return img


def create_photo(img):
    wpercent = (500/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((500, hsize), Image.ANTIALIAS)
    img = create_square(img)
    return img


def create_square(img, fill_color=(255, 255, 255, 0)):
    x, y = img.size
    size = max(x, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(img, (int((size - x) / 2), int((size - y) / 2)))
    new_im = new_im.convert("RGB")
    return new_im


def old_national():
    for files in os.listdir(ARCHIVES_DIRECTORY):
        thumbnail_path = 'archives/' + files + '/thumbs'
        if not os.path.exists(thumbnail_path):
            os.mkdir(thumbnail_path)
        for keyword in os.listdir(os.path.join(ARCHIVES_DIRECTORY, files)):
            keyword_path = os.path.join(ARCHIVES_DIRECTORY, files, keyword)
            folder = os.listdir(keyword_path)
            print(keyword)
            for image in folder:
                folder = os.listdir(keyword_path)
                if keyword != "thumbs":
                    image_path = os.path.join(keyword_path, image)
                    if not (any((keyword + ".jpg") in s for s in folder)):
                        if image[-4:] == '.jpg' or image[-4:] == '.png' or image[-5:] == '.jpeg' or image[-4:] == '.JPG' or image[-4:] == '.jfif':
                            image_path = os.path.join(keyword_path, image)
                            if os.path.isfile(image_path):
                                img = Image.open(image_path)
                                photo = create_photo(img)
                                print(keyword)
                                string_nova = ''.join(ch for ch in unicodedata.normalize('NFKD', keyword) 
                                    if not unicodedata.combining(ch))
                                print(string_nova)
                                photo.save(os.path.join(keyword_path, string_nova) + '.jpg', "JPEG")
                                thumb = create_thumb(photo)
                                thumb.save(os.path.join(keyword_path, string_nova) + '-thumb.jpg', "JPEG")
                                thumb.save(os.path.join(thumbnail_path, string_nova) + '.jpg', "JPEG")
    return


def resize(img):
    images = []

    img = create_photo(img)
    images.append(img)
    img = create_thumb(img)
    images.append(img)

    return images


def nacional():
    if not os.path.exists(thumbnail):
        os.mkdir(thumbnail)
    for company in os.listdir(directory):
        keywords = [keyword for keyword in os.listdir(os.path.join(directory, company))]
        extensions = ['.jpg', '.png', '.JPG', '.jfif', '.jpeg']
        for key in keywords:
            path = os.path.join(directory, key)
            if key != 'thumbs':
                all_imgs = os.listdir(os.path.join(directory, company, key))
                for img in all_imgs:
                    img, extension = os.path.splitext(img)
                    if any(x in extension for x in extensions):
                        print(key, img)
                        # open_img = Image.open(os.path.join(directory, key, img))
                        # resized_img = resize(open_img)
                        # resized_img[0].save(os.path.join(path, key) + '.jpg', 'JPEG')
                        # resized_img[1].save(os.path.join(path, key) + '-thumb.jpg', 'JPEG')
                        # resized_img[1].save(os.path.join(thumbnail, key) + '.jpg', 'JPEG')
    return


def logo():
    if not os.path.exists(thumbnail):
        os.mkdir(thumbnail)

    logo = Image.open(r'./archives/favicon.png')
    img = resize(logo)

    ignored = {"favicon.png"}
    keywords = [keyword for keyword in os.listdir(directory) if keyword not in ignored]

    for key in keywords:
        path = os.path.join(directory, key)
        img[0].save(os.path.join(path, key) + '.jpg', "JPEG")
        img[1].save(os.path.join(path, key) + '-thumb.jpg', "JPEG")
        img[1].save(os.path.join(thumbnail, key) + '.jpg', "JPEG")

    return


old_national()