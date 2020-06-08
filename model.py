from __future__ import division
import tensorflow as tf

def getmodel():
    model = tf.keras.models.load_model('vgg16bnus3.h5')
    model.compile(loss='binary_crossentropy',metrics = ['accuracy'])
    return model

