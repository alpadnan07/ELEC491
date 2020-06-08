import shutil as sh
import os

def categorize(path, labelnames):
    createLabelFolders(labelnames)
    f = open("Data Labels.txt","r")
    lines = f.readlines()
    for line in lines:
        strarr = line.split()
        filename = strarr[0]+".jpg"
        abnormality = strarr[1]
        if abnormality == '1':
            label = labelnames[0]
        else:
            label = labelnames[1]
        try:
            sh.copy(path+"/"+filename, label)
        except Exception as e:
            print("gerçek bir hata degil bu resim bu kategoriye ait degil diyor umursama",e)
def createLabelFolders(labelnames):
    try:
        os.mkdir(labelnames[0])
        os.mkdir(labelnames[1])
        print("label folders created")
    except:
        print("label folders already exists ")