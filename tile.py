import cv2 as cv
import numpy as np
import os

def tile(path, newpath,numtile):

    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")

    for item in dirs:
        filename = path+"/"+item
        image = cv.imread(filename)
        print("item",item)
        height, width,_ = image.shape
        print(image.shape)
        dx = int(width/numtile)
        dy = int(height / numtile)
        xarr = np.linspace(start = 0 ,stop = width - dx,num = numtile,dtype=int)
        yarr = np.linspace(start=0, stop= height - dy, num=numtile, dtype=int)
        for y in yarr:
            for x in xarr:
                imtile = image[y:y+dy,x:x+dx,:]
                newfilename = newpath + "/" + "tiled" + str(y) + str(x) + "-" + item
                cv.imwrite(newfilename, imtile)


    return 0
