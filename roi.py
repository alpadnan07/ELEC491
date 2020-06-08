import cv2, os

def croproi(filename, newfilename):
    import numpy as np
    image = cv2.imread(filename, 0)

    h,w = image.shape
    hmin = int(h/50)
    hmax = h - int(h/50)
    wmin = int(w/50)
    wmax = w - int(w/50)
    image = image[hmin:hmax,wmin:wmax]

    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

    # Find contour and sort by contour area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    """
    mask = np.zeros(image.shape, np.uint8)
    mask = cv2.drawContours(mask, [cnts[0]], 0, 255, -1)
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    """
    if len(cnts) == 0:
        return
    x, y, w, h = cv2.boundingRect(cnts[0])
    mask = np.zeros(image.shape,np.uint8)
    mask = cv2.drawContours(mask,[cnts[0]],0,255,-1)
    image = cv2.bitwise_and(image,image,mask)
    ROI = image[y:y + h, x:x + w]
    """
    cv2.imshow('ROI', ROI)
    cv2.imwrite('ROI.png', ROI)
    cv2.waitKey()
    """
    cv2.imwrite(newfilename,ROI)
    return 0

def roi(path, newpath):
    dirs = os.listdir(path)
    try:
        os.mkdir(newpath)
    except:
        print("folder "+newpath+" exists")
    for item in dirs:
        filename = path+"/"+item
        newfilename = newpath+"/"+item
        croproi(filename,newfilename)



