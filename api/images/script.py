import os, glob
from PIL import Image


THUMBNAIL_DIRECTORY = r'./uploads/thumbnails'
UPLOAD_DIRECTORY = r'./uploads/'

if not os.path.exists(THUMBNAIL_DIRECTORY):
    os.makedirs(THUMBNAIL_DIRECTORY)


def square(im, min_size=300, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


def thumbnail():
    basewidth = 300
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            img = Image.open(path)
            new_image = square(img)
            rgb_im = new_image.convert('RGB')
            # wpercent = (basewidth/float(img.size[0]))
            # hsize = int((float(img.size[1])*float(wpercent)))
            # img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            rgb_im.save(os.path.join(THUMBNAIL_DIRECTORY, filename) + '.jpg', "JPEG")


thumbnail()