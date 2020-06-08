from PIL import Image
import os, sys
import cv2
import numpy as np
import gcnimage as gcni
import gcnalp
def gcn(path,newpath):

    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("file already exist")

    for item in dirs:
        if os.path.isfile(path+'/'+item):
            f, e = os.path.splitext(path+'/'+item)
            img = cv2.imread(path+'/'+item)
            img,_,_ = cv2.split(img)
            #img = gcni.global_contrast_normalize(img)
            img = gcnalp.gcnim(img)
            filename = newpath+'/'+item
            cv2.imwrite(filename,img)