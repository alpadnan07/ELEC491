import cv2 as cv
import numpy as np
import random
from datetime import datetime
random.seed(datetime.now)
import os

def translate(path, newpath,delta):
    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")
    for item in dirs:
        filename = path+"/"+item
        image = cv.imread(filename)
        height, width = image.shape[:2]
        dx = random.randint(1,delta)
        dy = random.randint(1, delta)
        newfilename = newpath+"/"+"translatedx"+str(dx)+"dy"+str(dy)+item
        T = np.float32([[1, 0, dx], [0, 1, dy]])
        img_translation = cv.warpAffine(image, T, (width, height))
        cv.imwrite(newfilename, img_translation)
    return 0
