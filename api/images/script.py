import os
from PIL import Image


UPLOAD_DIRECTORY = r'./uploads/'
THUMBNAIL_DIRECTORY = r'./uploads/thumbnails'
PHOTO_DIRECTORY = r'./uploads/photos'


def thumbnail(img):
    wpercent = (300/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((300, hsize), Image.ANTIALIAS)
    return img


def photo(img):
    wpercent = (500/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((500, hsize), Image.ANTIALIAS)
    return img


def square(im, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(x, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


for filename in os.listdir(UPLOAD_DIRECTORY):
    path = os.path.join(UPLOAD_DIRECTORY, filename)
    if os.path.isfile(path):
        img = Image.open(path)

        thumb = thumbnail(img)
        thumb = square(thumb)
        thumb.save(os.path.join(THUMBNAIL_DIRECTORY, filename) + '.png', "PNG")

        ph = photo(thumb)
        ph.save(os.path.join(PHOTO_DIRECTORY, filename) + '.png', "PNG")
