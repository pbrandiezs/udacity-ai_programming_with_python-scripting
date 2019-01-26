import numpy as np 

# Activation (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


choices = [[2, 6, -2],
          [3, 5, -2.2],
          [5, 4, -3]]

for w1, w2, b in choices:
    probability = w1 * 0.4 + w2 * 0.6 + b
    print("w1: {}, w2: {}, b: {}, probability: {}, sigmoid_probability: {}".format(w1, w2, b, probability, sigmoid(probability)))

