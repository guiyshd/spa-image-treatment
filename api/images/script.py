import os, glob
from PIL import Image


def resize():
    basewidth = 300

    for infile in glob.glob(r'.\uploads\*.jpg'):
        try:
            file, ext = os.path.splitext(infile)
            img = Image.open(infile)

            print(file, "Antes", img.size)

            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            
            print(file, "Depois", img.size) 

            img.save(file + '.jpg', "JPEG")
        except IOError:
            print("Cannot create thumbnail for '%s'" % infile)
    return print("Funfou")