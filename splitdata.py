import os
import shutil as sh

def splitdata(path,trainpath,validationpath,validationpercent):
    try:
        os.mkdir(trainpath)
        os.mkdir(validationpath)
    except:
        print("files already exist")
    dirs = os.listdir(path)
    size = len(dirs)
    validationsize = int(size*validationpercent)
    trainsize = size - validationsize
    validationdirs = dirs[0:validationsize]
    traindirs = dirs[validationsize:]
    print(len(traindirs))
    for item in validationdirs:
        sh.copy(path+"/"+item,validationpath)
    for item in traindirs:
        sh.copy(path+"/"+item,trainpath)
