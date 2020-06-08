import cv2 as cv
import numpy as np
import random
from datetime import datetime
random.seed(datetime.now)
import os

def reflect(path, newpath,axis):
    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")
    for item in dirs:
        filename = path+"/"+item
        newfilename = newpath + "/" + "reflected" + str(axis)+ item
        image = cv.imread(filename)
        reflected = cv.flip(image,axis)

        cv.imwrite(newfilename, reflected)
    return 0
