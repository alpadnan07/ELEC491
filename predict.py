import os
import cv2 as cv
import model
import preprocessforpredict as preprocess
import shutil
import numpy as np
import tensorflow as tf

def predict(filename,m = None):
    print(filename)
    foldername = filename[:-4]


    try:
        os.mkdir(foldername)
        shutil.copy(filename, foldername)
    except:
        print("")
    preprocess.preprocess(foldername)
    if m is None:
        m = model.getmodel()

    results = []
    dirs = os.listdir(foldername+"/"+"resized")

    i = 0
    results = []
    for item in dirs:

        image = cv.imread(foldername+"/resized/"+item,cv.IMREAD_GRAYSCALE)

        image = image /255.

        h,w = image.shape
        image = tf.convert_to_tensor(image.reshape(h,w,1))
        image = tf.image.per_image_standardization(image)
        image = image.numpy()

        datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            samplewise_std_normalization = True,
            samplewise_center = True
        )

        image = datagen.standardize(image)
        try:
            image = image.reshape(1,299,299,1)
        except:
            continue
        result = m.predict(image)
        print(result[0])
        results.append(result[0])
    shutil.rmtree(foldername)

    prediction = np.mean(results)
    return prediction
