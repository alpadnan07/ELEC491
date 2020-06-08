import cv2
import os
import shutil as sh
def roi2(path, newpath):
    try:
        os.mkdir(newpath)
    except:
        print("folder is not created")
    f = open("Info.txt","r")
    lines = f.readlines()
    for line in lines:
        strarr = line.split()
        if len(strarr) != 7:
            continue
        filename = strarr[0]+".jpg"
        x = strarr[4]
        x = int(x)
        y = strarr[5]
        y = int(y)
        r = strarr[6]
        r = int(r)
        if not(isinstance(x, int) and isinstance(x, int) and isinstance(x, int)):
            continue

        img = cv2.imread(path + '/' + filename)
        shape = img.shape
        h = shape[0]
        newimg = img[(y-r):(y+r),(x-r):(x+r),:]
        cv2.imwrite(newpath+"/"+filename, newimg)