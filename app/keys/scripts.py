import os
from PIL import Image
from unidecode import unidecode

import imghdr


ARCHIVES_DIRECTORY = r'./archives'
directory = r'./archives'
thumbnail = r'./archives/thumbs'


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


def national():
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
                                unidecode(keyword)
                                photo.save(os.path.join(keyword_path, keyword) + '.jpg', "JPEG")
                                thumb = create_thumb(photo)
                                thumb.save(os.path.join(keyword_path, keyword) + '-thumb.jpg', "JPEG")
                                thumb.save(os.path.join(thumbnail_path, keyword) + '.jpg', "JPEG")
    return


def resize(img):
    images = []

    img = create_photo(img)
    images.append(img)
    img = create_thumb(img)
    images.append(img)

    return images

0
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


national()