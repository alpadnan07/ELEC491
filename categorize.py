import shutil as sh
import os

def categorize(path, newpath):
    createLabelFolders()
    f = open("Data Labels.txt","r")
    lines = f.readlines()
    for line in lines:
        print(line)
        strarr = line.split()
        filename = strarr[0]+".jpg"
        print("filetype",strarr[0])
        filetype = strarr[1]
        try:
            sh.copy(path+"/"+filename, filetype)
        except Exception as e:
            print(e)
def createLabelFolders():
    try:
        os.mkdir("1")
        os.mkdir("2")
        os.mkdir("3")
    except:
        print("label folders already exists ")