import numpy as np
def gcnim(X):
    mean = np.mean(X)
    height = X.shape[0]
    width = X.shape[1]
    X = X- mean
    print(X)
    X = X.reshape(height,width,1)
    return X