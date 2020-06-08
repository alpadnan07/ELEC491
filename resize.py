#!/usr/bin/python
from PIL import Image
import os, sys,numpy

def resize(path, newpath, newsizex,newsizey):
    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
        print("folder "+newpath+" created")
    except:
        print("folder "+newpath+" exists")
    for item in dirs:
        if os.path.isfile(path+"/"+item):
            im = Image.open(path+"/"+item)
            f, e = os.path.splitext(newpath+"/"+item)
            imResize = im.resize((newsizex,newsizey), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)
#resize()
def dividesize(path, newpath,ratio):
    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
        print("folder "+newpath+" created")
    except:
        print("folder "+newpath+" exists")
    for item in dirs:
        if os.path.isfile(path+"/"+item):
            im = Image.open(path+"/"+item)
            f, e = os.path.splitext(newpath+"/"+item)
            x, y = im.size
            y = int(y/ratio)
            x = int(x/ratio)
            imResize = im.resize((y,x), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)