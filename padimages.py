import os
import cv2
import numpy as np
def getMaximumBorders(path):
    dirs = os.listdir(path)
    maxwidth = 0
    maxheight = 0
    for item in dirs:
        print(item)
        image = cv2.imread(path+"/"+item, 0)
        shape = image.shape
        print(shape,item)
        height = shape[0]
        width = shape[1]
        if width > maxwidth:
            maxwidth = width
        if height> maxheight:
            maxheight = height
    return maxheight, maxwidth
def padImagesToShape(path,newpath ,maxheight, maxwidth):
    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("")
    for item in dirs:
        image = cv2.imread(path+"/"+item, 0)
        height,width = np.shape(image)
        dheight = maxheight - height
        dwidth = maxwidth - width
        sameShapeImage = cv2.copyMakeBorder(image, dheight, 0, dwidth, 0, cv2.BORDER_CONSTANT,value = 0)
        print(newpath+'/' + item)
        cv2.imwrite(newpath+'/' + item, sameShapeImage)
def padImages(path,newpath):
    maxheight, maxwidth = getMaximumBorders(path)
    padImagesToShape(path,newpath ,maxheight, maxwidth)

