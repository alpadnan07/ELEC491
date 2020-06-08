import os
import predict
import numpy as np
import model

path = "2testmiasv2"
dirs = os.listdir(path)
size = len(dirs)
results = []


m = model.getmodel()
for item in dirs:
    prediction = predict.predict(path + "/" + str(item), m)
    results.append(prediction)
    print("RESULT", np.mean(results))
#print("predictions",results)
