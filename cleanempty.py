import cv2 as cv
import numpy as np
import os

def cleanempty(path, newpath):

    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")

    dirs = os.listdir(path)
    for item in dirs:
        filename = path+"/"+item
        image = cv.imread(filename)
        height,width,_ = image.shape
        area = height*width
        num0 = (image < 10).sum()
        num255 = (image == 255).sum()
        if num0 > area*1/10:
            continue
        if num255 > area*9/10:
            continue

        newfilename = newpath + "/" + item
        cv.imwrite(newfilename, image)

    return 0
