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

def list_to_weights(lis, shape=[27, 16, 16, 4]):
    weights = []
    index = 0
    for i in range(len(shape) - 1):
        row = []
        dx = shape[i]
        for j in range(shape[i+1]):
            row.append(weights[index:index + dx])
            index += dx
        weights.append(row)
    return weights

def list_to_biases(lis, shape=[27, 16, 16, 4]):
    biases = []
    index = 0
    for i in shape[1:]:
        biases.append(shape[index: index + i])
        index += i
    return biases

if __name__ == "__main__":
    weights = [[[1, 2, 3], [2, 1, 4]],
               [[-5, 7], [4, -3]],
               [[1, -1]]]
    biases = [[4, -3], [3, 1], [-2]]
    lis = [1, 2, 3, 2, 1, 4, -5, 7, 4, -3, 1, -1]
    weights2 = list_to_weights(lis, [3, 2, 2, 1])
    lis = [4, -3, 3, 1, -2]
    biases2 = list_to_biases(lis, [3, 2, 2, 1])
    nn = NeuralNet(weights, biases)
    nn2 = NeuralNet(weights2, biases2)
    for i in range(-5, 5):
        print(nn.compute([i-1, i, i+1])[0] - nn2.compute([i-1, i, i+1])[0])
        # should be all zeros.
