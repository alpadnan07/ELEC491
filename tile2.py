import cv2 as cv
import numpy as np
import os

def tile(path, newpath,delta):

    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")

    for item in dirs:
        filename = path+"/"+item
        image = cv.imread(filename)
        height, width,_ = image.shape
        xframe = delta
        yframe = delta

        dx = delta
        dy = delta
        y = 0
        x = 0
        while y+yframe <height:
            while x+xframe<width:
                imtile = image[y:y+yframe,x:x+xframe,:]
                newfilename = newpath + "/" + "tiled" + str(y) + str(x) + "-" + item
                cv.imwrite(newfilename, imtile)
                x += dx
            y += dy
            x = 0
    return 0
