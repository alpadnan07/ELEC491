import rotate as rot
import translate as trans
import reflect as ref
import copydir
def augment(path,newpath,augmentation_paramaters):

    for parameter in augmentation_paramaters:
        if "rotation-" in parameter:
            parameter = parameter.replace("rotation-","")
            angle = int(parameter)
            rot.rotate(path,newpath,angle)
        elif "translation-" in parameter:
            parameter = parameter.replace("translation-","")
            delta = int(parameter)
            trans.translate(path,newpath,delta)
        elif "reflection-" in parameter:
            parameter = parameter.replace("reflection-","")
            axis = 0 if parameter == "x" else 1
            ref.reflect(path,newpath,axis)
        else:
            print("invalid parameter")
        copydir.copyDirectory(path,newpath)