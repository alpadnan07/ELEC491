from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import tensorflow.keras.backend as K
import numpy as np
import cv2
import sys
import model as modelb
import os

model = modelb.getmodel()
model.summary()
os._exit(0)
img_path = sys.argv[1]
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)