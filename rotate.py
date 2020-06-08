from PIL import Image
import os, sys
import cv2 

def rotate(path,newpath,angle):

    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")

    for item in dirs:
        if os.path.isfile(path+'/'+item):
            f, e = os.path.splitext(path+'/'+item)
            img = cv2.imread(path+'/'+item)
            h, w, c = img.shape
            center = (w/2,h/2)
            scale = 1.0

            M = cv2.getRotationMatrix2D(center,angle,scale)
            abs_cos = abs(M[0,0])
            abs_sin = abs(M[0,1])
            bound_w = int(h * abs_sin + w * abs_cos)
            bound_h = int(h * abs_cos + w * abs_sin)
            M[0,2] += bound_w/2 - center[0]
            M[1,2] += bound_h/2 - center[1]
            rotated = cv2.warpAffine(img, M, (bound_w,bound_h))
            filename = newpath+'/'+'rotated_'+str(angle)+item
            cv2.imwrite(filename,rotated)
