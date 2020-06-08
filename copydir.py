import shutil as sh
import os
def copyDirectory(path,newpath):
    dirs = os.listdir(path)
    for item in dirs:
        sh.copy(path+"/"+item,newpath)
