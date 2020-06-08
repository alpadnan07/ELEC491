import cv2 as cv
import os

def histogrameq(path, newpath):
    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")
    for item in dirs:
        filename = path+"/"+item
        newfilename = newpath+"/"+item
        image = cv.imread(filename, 0)
        equilized = cv.equalizeHist(image)
        cv.imwrite(newfilename, equilized)
    return 0
