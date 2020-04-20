import os, json
import scipy.spatial
import numpy as np
cdist = scipy.spatial.distance.cdist

TOP = 4
epoch = 25
vectors = []
while os.path.isfile(f"saved_weights/epoch{epoch}.json"):
    with open(f"saved_weights/epoch{epoch}.json") as f:
        data = json.load(f)
    vectors.append(np.array([list(weights.values()) for weights in data[:TOP]]))
    epoch += 1

dists = [cdist(vectors[i], vectors[i+1]) for i in range(len(vectors)-1)]
min_dists = [(dist.min(axis=0)**2).sum() for dist in dists]
print(min_dists)
