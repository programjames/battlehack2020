import math

def sigmoid(x):
    return 1/(1+math.exp(-x))
def sigmoid_list(x):
    return [1/(1+math.exp(-v)) for v in x]

def dot(x, y):
    return sum(a*b for a,b in zip(x,y))

def vector_sum(x, y):
    return [a+b for a,b in zip(x,y)]

class NeuralNet():
    def __init__(self, weights, biases):
        self.weights = weights
        self.biases = biases
    def compute(self, inputs):
        v = inputs[:]
        for weight, b in zip(weights, biases):
            v = [dot(v, w) for w in weight]
            v = vector_sum(v, b)
            v = sigmoid_list(v)
        return v

def generate_weights(shape=[25, 16, 16, 4]]:
    weights = []
    c = 0
    for i in range(len(shape) - 1):
        s = shape[i]
        t = shape[i+1]
        weights.append()
        c += 1

if __name__ == "__main__":
    weights = [[[1, 2, 3], [2, 1, 4]],
               [[-5, 7], [4, -3]],
               [[1, -1]]]
    biases = [[4, -3], [3, 1], [-2]]
    nn = NeuralNet(weights, biases)
    for i in range(-5, 5):
        print(nn.compute([i-1, i, i+1]))
